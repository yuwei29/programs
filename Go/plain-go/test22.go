package main

import "fmt"

func sum(a int, b int, c chan int) {
	res := 0
	for i := a; i < b; i++ {
		res += i
	}
	c <- res
}
func main() {
	c := make(chan int)
	go sum(0, 50, c)
	go sum(50, 100, c)
	x, y := <-c, <-c
	fmt.Println(x, y, x+y)
}
