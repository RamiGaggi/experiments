package main

import "fmt"


func main() {
	fmt.Println(ChangeSLice(3, 4))
}

func ChangeSLice(sl ...int) int {
	return sl
}
