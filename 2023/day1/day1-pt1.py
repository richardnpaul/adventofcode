#!/usr/bin/env python3

def get_calibration_values(line):
    numbers = [char for char in line if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    if len(numbers) == 1:
        concatinated_numbers = numbers[0] + numbers[0]
    elif len(numbers) >= 2:
        concatinated_numbers = numbers[0] + numbers[-1]
    else:
        print("something went wrong")
        exit(1)
    return int(concatinated_numbers)


with open("input.txt") as f:
    lines = f.readlines()
    value = 0
    for line in lines:
        if len(line) != 0:
            value += get_calibration_values(line)
    print(value)
