// Write a golang function that takes a file containing a list of numbers separated by newlines
// and sums groups of numbers separated by double newlines for example, given the following file:
// 1000
// 2000
// 3000
//
// 4000
//
// 5000
// 6000
//
// 7000
// 8000
// 9000
//
// 10000
// the result should be an array of 5 numbers: [6000, 4000, 10000, 24000, 10000]
// the main function should then pick the largest number and print it

package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var sum int
	var sums []int

	reader := bufio.NewScanner(file)
	reader.Split(bufio.ScanLines)
	for reader.Scan() {
		line, err := reader.Text(), reader.Err()
		if err != nil && err != io.EOF {
			log.Fatal(err)
		}

		if line != "" {
			line = strings.TrimSuffix(line, "\n")
			num, err := strconv.Atoi(line)
			if err != nil {
				log.Fatal(err)
			}
			sum += num
		} else {
			sums = append(sums, sum)
			sum = 0
		}

		if err == io.EOF {
			break
		}
	}

	var max int
	var pos int
	pos = 1
	for _, sum := range sums {
		if sum > max {
			max = sum
			pos = pos + 1
		}
	}

	fmt.Println(pos)
}
