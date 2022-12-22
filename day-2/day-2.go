package main

import "fmt"

func main() {
	// Create a map to store the score of each hand shape
	scores := map[byte]int{'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

	// Initialize the total score to 0
	totalScore := 0

	// Read the strategy guide from the input
	var opponentHand, myHand byte
	for {
		_, err := fmt.Scanf("%c %c\n", &opponentHand, &myHand)
		if err != nil {
			break
		}

		// Calculate the score for this round
		roundScore := scores[myHand]
		if scores[myHand] == scores[opponentHand] {
			roundScore += 3
		} else if (myHand == 'X' && opponentHand == 'C') || (myHand == 'Y' && opponentHand == 'A') || (myHand == 'Z' && opponentHand == 'B') {
			roundScore += 6
		}

		fmt.Printf("Opponent: %c My hand: %c Score: %d\n", opponentHand, myHand, roundScore)

		// Add the score for this round to the total score
		totalScore += roundScore
	}

	// Print the total score
	fmt.Println(totalScore)
}
