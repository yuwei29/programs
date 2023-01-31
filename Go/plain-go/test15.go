package main
import "fmt"
func f1(x int) int{
  return 2*x+5
}
func f2(s string,a int,f func(int) int){
  
  fmt.Println(s,f(a))
}

func main(){
   f2("Hello",3,f1)
   var f3 = func(a int)int{ return 30*a}
   f2("world",3,f3)
}
  