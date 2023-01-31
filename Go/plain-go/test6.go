package main

import "fmt"
type Student struct{
    name string
    yu int
    shu int
    ying int
}
func (s Student) String() string{
    return fmt.Sprintf("%v %v %v %v",s.name,s.yu,s.shu,s.ying)
}
func main(){
    var n int
    var dalao Student
    //var high int = 0 这里有错，没考虑所有人分数全0的情况
	var high int = -1
    fmt.Scanln(&n)
    for i:=0;i<n;i++{
        var name string
        var y,s,yi int
        fmt.Scanln(&name,&y,&s,&yi)
        if fen:=y+s+yi;fen > high{
            high = fen
            dalao = Student{name,y,s,yi}
        }
    }
    fmt.Println(dalao)
}