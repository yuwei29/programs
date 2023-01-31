package main

import "fmt"

func sum(a []int,c chan int){
  res:=0
  for _,v:=range a{
    res+=v
  }
  c<-res
}
func main(){
  a:=[]int{1,2,3,4,5,6,7,8,9,10}
  c:=make(chan int)
  go sum(a[:5],c)
  go sum(a[5:],c)
  x,y:=<-c,<-c 
  fmt.Println(x,y,x+y)
}