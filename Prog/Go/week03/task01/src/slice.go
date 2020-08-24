package main

import (
	"fmt"
	"strconv"
)

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
	for {
		//var res [3]int
		//var res [3]int
		res := make([]int, 3)
		var s string
		//fmt.Scanln(&s)
                for i:=0;i<3;i++ {
	                fmt.Scanln(&s)
			if s == "X" {
				fmt.Println("Terminado")
				break
			} else{
				//ss,_ :=strconv.Atoi(s)
				//for i:=0;i<3;i++ {
				res[i],_=strconv.Atoi(s)
				//}
				fmt.Println(SortA(res))
				fmt.Println(res)
				//fmt.Println(ss)
				//a :=[]int{2,1232,2,3,22,212}
				//fmt.Println(SortA(a))
			}
		}
	}

}
