package main

import "fmt"

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))    // [1 2 4]
	fmt.Println(plusOne([]int{9, 9, 9}))    // [1 0 0 0]
	fmt.Println(plusOne([]int{4, 3, 2, 1})) // [4 3 2 2]
}