package main
import (
	"fmt"
	"os"
	"bufio"
)

func main(){
	var s string
	reader := bufio.NewReader(os.Stdin)
	for {
		strBytes,_,_ := reader.ReadLine()
		s = string(strBytes)
		fmt.Println(s)
		
	}
}