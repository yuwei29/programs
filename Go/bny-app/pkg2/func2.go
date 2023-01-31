package pkg2

import "bny-app/pkgtest1"

func Func2() (string, int) {
	return pkgtest1.Func1(3, "output-from-func2")
}
