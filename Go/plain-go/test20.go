package main
import(
	"fmt"
	"reflect"
) 
func main(){
	s:="this is a sentence"
	fmt.Println(reflect.TypeOf(s[2]))
}