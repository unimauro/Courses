package main

import "fmt"

//Burble
func SortA(x []int) []int {
	for i:=len(x);i>0;i-- {
		for j:=1;j<i;j++{
			if x[j-1] > x[j] {
				inter :=x[j]
				x[j] =x[j-1]
				x[j-1] = inter
			}
		}
	}
	return x
}

func main () {
	a :=[]int{2,1232,2,3,22,212}
	fmt.Println(SortA(a))
}
