package ch1

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	EchoArgs2()
}

func EchoArgs1() {
	fmt.Println(strings.Join(os.Args[:], "$$"))
}


func EchoArgs2() {
	for i, arg := range os.Args[:] {
		fmt.Println(i, arg)
	}
}

func EchoArgs3() {
	for i, arg := range os.Args[:] {
		fmt.Println(i, arg)
	}
}

func EchoArgs4() {
	s, sep := "", ""
	for _, arg := range os.Args {
		s += sep + arg
		sep = "^^"
	}
}
