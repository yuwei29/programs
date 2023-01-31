package main
import (
  "fmt"
  "time"
)

func main(){
   start:=time.Now()
   sum:=0
   for i:=0;i<1e9;i++{
     sum+=i 
   }
   cost:=time.Since(start)
   fmt.Println("exec cost is",cost)
}