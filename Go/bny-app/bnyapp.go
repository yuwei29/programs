package main

import (
	"bny-app/pkg2"
	"bny-app/pkgtest1"
	"fmt"

	"rsc.io/quote"
)

func main() {
	a := 10
	b := "longlongago"
	fmt.Println(pkgtest1.Func1(a, b))
	fmt.Println(pkg2.Func2())
	fmt.Println(quote.Go())
}
