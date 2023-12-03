#!/usr/bin/env python3
import re
import sys

def get_calibration_values(line):
    numbers = [char for char in line if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    if len(numbers) == 1:
        concatinated_numbers = numbers[0] + numbers[0]
    elif len(numbers) >= 2:
        concatinated_numbers = numbers[0] + numbers[-1]
    else:
        print("something went wrong")
        exit(1)
    print(concatinated_numbers)
    return int(concatinated_numbers)


# normalise the input, replace numbers in the text, e.g. one to 1, two to 2, etc.
def normalise_input(line):
    if len(line) <= 2:
        return line

    for num in [("one", "one1one"), ("two", "two2two"), ("three", "three3three"), ("four", "four4four"), ("five", "five5five"), ("six", "six6six"), ("seven", "seven7seven"), ("eight", "eight8eight"), ("nine", "nine9nine")]:
        if num[0] in line:
            line = re.sub(num[0], num[1], line)

    return line


with open(sys.argv[1]) as f:
    lines = f.readlines()
    value = 0
    for line in lines:
        if len(line) != 0:
            normalised_line = normalise_input(line)
            value += get_calibration_values(normalised_line)
    print(value)
