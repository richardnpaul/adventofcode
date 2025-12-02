package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func processLine(line string, current_value int) int {
	// Process the line
	letter := line[:1]
	numStr := line[1:]
	num, err := strconv.Atoi(numStr)
	if err != nil {
		log.Printf("Error converting number: %v", err)
	}

	switch letter {
	case "L":
		current_value -= num
	case "R":
		current_value += num
	}

	if current_value < 0 {
		current_value %= 100
		if current_value < 0 {
			current_value += 100
		}
	} else if current_value > 99 {
		current_value %= 100
	}

	log.Printf("Processed Line: %s, New Value: %d", line, current_value)
	return current_value
}

func main() {

	current_value := 50
	zero_counter := 0

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		if strings.TrimSpace(line) == "" {
			continue
		}

		process_output := processLine(line, current_value)
		if process_output == 0 {
			zero_counter++
		}
		current_value = process_output
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	log.Printf("Final Value: %d", zero_counter)
}
