package main

import (
	"fmt"
	"strconv"
)

func main() {
	var accl, velo, disp, time float64
	accl = takeFloatInput("Enter acceleration: ")
	velo = takeFloatInput("Enter velocity: ")
	disp = takeFloatInput("Enter displacement: ")

	displacefn := GenDisplaceFn(accl, velo, disp)
	time = takeFloatInput("Enter time: ")
	fmt.Println(displacefn(time))
}

func takeFloatInput(text string) float64 {
	for {
		var input string
		fmt.Print(text)
		_, err := fmt.Scanln(&input)

		if err != nil {
			fmt.Printf("Error with input '%s'. Try gain!!!\n\n", input)
		} else {
			if finput, ferr := strconv.ParseFloat(input, 64); ferr != nil {
				fmt.Printf("Can not convert '%s' to float. Try again!!!\n\n", input)
			} else {
				return finput
			}

		}

	}
}

// GenDisplaceFn produce a function that calculate Displacement as
// 1/2 * accelation * sq(t) + ivelocity * t + idisplacement
func GenDisplaceFn(accelation float64, ivelocity float64, idisplacement float64) func(float64) float64 {
	return func(time float64) float64 {
		return (0.5)*accelation*time*time + ivelocity*time + idisplacement
	}
}
