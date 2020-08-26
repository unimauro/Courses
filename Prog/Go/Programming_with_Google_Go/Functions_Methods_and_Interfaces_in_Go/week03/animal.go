package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Animal struct {
	food       string
	locomotion string
	sound      string
}

func (animal Animal) Eat() {
	fmt.Println(animal.food)
}

func (animal Animal) Move() {
	fmt.Println(animal.locomotion)
}

func (animal Animal) Speak() {
	fmt.Println(animal.sound)
}

func getNewAnimal(input string) *Animal {
	switch input {
	case "cow":
		cow := &Animal{"grass", "walk", "moo"}
		return cow
	case "bird":
		bird := &Animal{"worms", "fly", "peep"}
		return bird
	case "snake":
		snake := &Animal{"mice", "slither", "hss"}
		return snake
	default:
		return nil
	}
}

func performAction(input string, animal Animal) {
	switch input {
	case "eat":
		animal.Eat()
	case "move":
		animal.Move()
	case "speak":
		animal.Speak()
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Printf(">")
		input, _ := reader.ReadString('\n')
		input = strings.ToLower(strings.TrimSuffix(input, "\n"))
		command := strings.Split(input, " ")

		animal := getNewAnimal(command[0])
		performAction(command[1], *animal)
	}
}
