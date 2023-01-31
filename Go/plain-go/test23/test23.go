package main

import (
	"fmt"
	"time"
)

func sum(a int, b int, c chan int) {
	res := 0
	for i := a; i < b; i++ {
		res += i
	}
	c <- res
}
func main() {
	start := time.Now()
	c := make(chan int)
	go sum(0, 500000000, c)
	go sum(500000000, 1000000001, c)
	x, y := <-c, <-c
	ans := x + y
	end := time.Now()
	dur := end.Sub(start)
	fmt.Println(dur.Nanoseconds())
	fmt.Println(ans)
}
