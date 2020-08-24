
package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
)

type name struct {
    fname string
    lname string
}

func main(){
    fmt.Println("Please before create a file (names.txt)  with a Name and a Lastname separed by a spice \n like: \n Marco Parra \n Hugo Baila \n ")
    read_input := bufio.NewScanner(os.Stdin)
    fmt.Printf("\nPlease filename containing a list: ")
    read_input.Scan()
    file_name := read_input.Text()
    
    file, err := os.Open(file_name)
    if err != nil {
        fmt.Println("\nFile could not be opened. Please")
        fmt.Println("correct filename and path before running again.")
    }

    name_slice := make([]name, 0)
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        name_strings := strings.Fields(scanner.Text())
        p := name{fname: name_strings[0], lname: name_strings[1]}
        name_slice = append(name_slice, p)
    }

    fmt.Println("\nHere are your list of names from", file_name)
 
    for i:=0; i<len(name_slice); i++{
        fmt.Println(name_slice[i].fname, name_slice[i].lname)
    }

}
