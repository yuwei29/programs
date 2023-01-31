package main
import "fmt"
type F func(int) int 
func F1(x int) int{
  return x+5
}
func F2(x int) int{
  return x*10
}
func main(){ 
  //var test = func() F{ return func(x){return x+13}} 
  //var compose = func(f,g F) F { return func(x){return f(g(x)) } } //源于https://blog.csdn.net/timczm/article/details/119219003 的错误写法
  //var t = test()
  //var F12 = compose(F1,F2)
  //fmt.Println(t(13))
  var F12 = func(x int) int { return F1(F2(x))}
  fmt.Println(F12(50))
}