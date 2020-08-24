package main

import(
	"fmt"
	"strings"
)


func main(){
	var s string 
	fmt.Println("Please write la variable:")
	fmt.Scanf("%s", &s)

	if strings.Contains(s,"i"){		
		fmt.Println("Found! \n")
	} else if strings.Contains(s,"a"){
                fmt.Println("Found! \n")
	} else if strings.Contains(s,"n"){       
                fmt.Println("Found! \n")
        } else{
                fmt.Println("Not Found! \n")
        }


}


