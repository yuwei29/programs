package main
import "fmt"

func main(){
    var n int
    fmt.Scan(&n)
    var a []int
    var b int
    for i:=0;i<n;i++{
        fmt.Scan(&b)
        a=append(a,b)
    }
    if(n==0){
        fmt.Println(0)
        return
    }
    res:=a[0]
    for i:=1;i<n;i++{
        {
            max:=a[i]
			s:=max
			for j:=i-1;j>=0;j--{
				s+=a[j]
				if s>max {
					max=s
				}
			}
			if max>res{
				res=max
			}
        }
        
    }
    fmt.Println(res)
}