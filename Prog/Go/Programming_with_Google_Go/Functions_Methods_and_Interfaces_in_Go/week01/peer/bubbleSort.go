package main

import "fmt"

func swap(vector []int, index int) {
	if len(vector)-1 <= index {
		return
	}

	vector[index] = vector[index] ^ vector[index+1]
	vector[index+1] = vector[index] ^ vector[index+1]
	vector[index] = vector[index] ^ vector[index+1]
}

func bubbleSort(vector []int) {
	n := len(vector)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-1-i; j++ {
			if vector[j] > vector[j+1] {
				swap(vector, j)
			}
		}
	}

}

func main() {
	var vector []int

	for i := 0; i < 10; i++ {
		var buffer int

		fmt.Println("Enter number: ")
		fmt.Scan(&buffer)

		vector = append(vector, buffer)
	}

	bubbleSort(vector)
	fmt.Println(vector)
}
