package main

import "fmt"

func (p *Point) sum() int{
   return p.x+p.y
}
type Point struct{
  x int
  y int
}
func f2(x int) int{
  return f1(x)+3
}
func f1(x int) int{
  return x+5
}
func main(){
   p := Point{3,4}
   fmt.Printf("%d\n",p.sum())
   fmt.Println(f2(10))

}