package main

import(
	"fmt"
	"strings"
)


func main(){
	var s string 
	fmt.Println("Please write the variable:\n")
	fmt.Scanfln(&s)

	if strings.Contains(s,"a") && (s[0]=='i' || s[0]=='I') && (s[len(s)-1]=='n' || s[len(s)-1]=='N') {
		fmt.Print("Found!")
	}else{
		fmt.Print("Not Found!")
	}

}


