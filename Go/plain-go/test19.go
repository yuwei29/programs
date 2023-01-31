package main
import "fmt"
/*
000...0
|

111...1
0--N-1位
选第i位不翻转
i越小 序号越前

A: 60   111100
B: 13   001101
A&B    001100   12
A|B      111101    61
A^B     110001   49

*/
var a,mir [100]int
var n,sum0,sum1 int
var state=true
var ok=false
func toggle(i int){
  tmp0,tmp1:=a[i],mir[i]
  a[i]^=1
  mir[i]^=1
  state=!state
  sum0+=(a[i]-tmp0)
  sum1+=(mir[i]-tmp1)
  if(state){
    if(sum0==n){ok=true}
  }else{
    if(sum1==n){ok=true}
  }
}
func printResult(){
if(state){
for i:=0;i<n;i++{
fmt.Printf("%d",a[i])
}
fmt.Println()
}else{
for i:=0;i<n;i++{
fmt.Printf("%d",mir[i])
}
fmt.Println()
}
}
func main(){
  fmt.Scanln(&n)
  fmt.Println(n)
  sum1=n
  for i:=0;i<n;i++{
     mir[i]=1
  }
  i:=0
  for !ok {
     toggle(i)
     i++
    printResult()
  }
}