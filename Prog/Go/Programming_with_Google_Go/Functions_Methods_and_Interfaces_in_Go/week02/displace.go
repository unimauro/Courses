package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func GenDisplaceFn(acceleration, initialVelocity, initialDisplacement float64) func(float64) float64 {
	function := func(time float64) float64 {
		return 0.5*acceleration*math.Pow(time, 2) + initialVelocity*time + initialDisplacement
	}
	return function
}

func getFloatInput() float64 {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.TrimSuffix(input, "\n")
	floatValue, _ := strconv.ParseFloat(input, 64)
	return floatValue
}

func promptAndGetValue(name string) float64 {
	fmt.Println("Enter value for " + name + ": ")
	return getFloatInput()
}

func main() {
	acceleration := promptAndGetValue("acceleration")
	initialVelocity := promptAndGetValue("initialVelocity")
	initialDisplacement := promptAndGetValue("initialDisplacement")
	time := promptAndGetValue("time")

	function := GenDisplaceFn(acceleration, initialVelocity, initialDisplacement)
	fmt.Println(function(time))
}


