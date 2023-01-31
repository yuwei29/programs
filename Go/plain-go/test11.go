package main
import "fmt"
func main(){
    var n,m int
    fmt.Scan(&n,&m)
    var a [][]rune
	fmt.Scanf("\n")
    for i:=0;i<n;i++{
        b:=[]rune{}
        for j:=0;j<m;j++{
            var c rune
            fmt.Scanf("%c",&c)
            b=append(b,c)
        }
		fmt.Scanf("\n")
        a = append(a,b)
    }
    for i:=0;i<n;i++{
        for j:=0;j<m;j++{
            if(a[i][j]=='?'){
                s:=0
                if i>0 {
                    if a[i-1][j]=='*'{s++}
                    if j>0 {if a[i-1][j-1]=='*'{s++}}
                    if j<m-1 {if a[i-1][j+1]=='*'{s++}}
                }
                if j>0 {
                    if a[i][j-1]=='*'{s++}
                    if i<n-1 {if a[i+1][j-1]=='*'{s++} }
                }
                if i<n-1 {
                    if a[i+1][j]=='*'{s++}
                    if j<m-1 {if a[i+1][j+1]=='*' {s++}}
                }
                if j<m-1 {
                    if a[i][j+1]=='*'{s++}
                }
                a[i][j]= rune(s+'0')
            }
            fmt.Printf("%c",a[i][j])
        }
        fmt.Printf("\n")
    }
}