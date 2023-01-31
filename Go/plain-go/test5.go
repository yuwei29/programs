package main

import "fmt"

func main(){
  a:=3<5&&3>2
  b:=3<5&&3>6
  if a||b{
    fmt.Println("a or b")
  }
  fmt.Println(a,b)
}