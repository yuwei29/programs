package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

func sum(a int, b int, c chan int) {
	res := 0
	for i := a; i < b; i++ {
		res += i
	}
	c <- res
}
func msum(l int, r int, idx int) int {
	start := time.Now()
	res := 0
	c := make(chan int)
	step := (r - l) / idx
	if (r-l)%idx != 0 {
		step++
	}
	r1 := r - step
	for ; l < r1; l += step {
		go sum(l, l+step, c)
	}
	go sum(l, r, c)
	for i := 0; i < idx; i++ {
		res += <-c
	}
	end := time.Now()
	dur := end.Sub(start)
	fmt.Println(dur.Nanoseconds())
	return res
}
func main() {
	ls, rs, idxs := os.Args[1], os.Args[2], os.Args[3]
	l, _ := strconv.Atoi(ls)
	r, _ := strconv.Atoi(rs)
	idx, _ := strconv.Atoi(idxs)
	ans := msum(l, r, idx)
	fmt.Println(ans)
}
