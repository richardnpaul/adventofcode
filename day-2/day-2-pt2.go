package main

import "fmt"

func main() {
	// Create a map to store the score of each hand shape
	// A = rock
	// B = paper
	// C = scissors
	scores := map[byte]int{'A': 1, 'B': 2, 'C': 3}

	// Initialize the total score to 0
	totalScore := 0

	// Read the strategy guide from the input
	var opponentHand, myHand byte
	for {
		n, err := fmt.Scanf("%c %c\n", &opponentHand, &myHand)
		if err != nil || n < 2 {
			break
		}

		var roundScore int
		if myHand == 'X' {
			// lose
			if opponentHand == 'A' {
				roundScore = 3
			} else if opponentHand == 'B' {
				roundScore = 1
			} else if opponentHand == 'C' {
				roundScore = 2
			} else {
				roundScore = 0
			}
		} else if myHand == 'Y' {
			// draw
			roundScore = scores[opponentHand] + 3
		} else if myHand == 'Z' {
			// win
			if opponentHand == 'A' {
				roundScore = 8
			} else if opponentHand == 'B' {
				roundScore = 9
			} else if opponentHand == 'C' {
				roundScore = 7
			} else {
				roundScore = 0
			}
		} else {
			roundScore = 0
		}

		// Add the score for this round to the total score
		totalScore += roundScore
	}

	// Print the total score
	fmt.Println(totalScore)
}
