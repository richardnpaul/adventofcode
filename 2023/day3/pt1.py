#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# problem
# given a matrix of characters, find any numbers which are adjacent to specific characters
# solution
# iterate through the matrix, if the character is a number, check if it is adjacent to a character
# if it is, add it to a list
# return the list

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

import re
from sys import argv


with open(argv[1], 'r') as f:
    lines = f.readlines()
    chars = []
    for line in lines:
        chars.extend(list(line))
    sorted_list = sorted(set(chars))

ignore_list = ['0', '1', '2', '3', '4', '5', '\n', '6', '7', '8', '9', '.']
symbols = [i for i in sorted_list if i not in ignore_list]

grid = []

with open(argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        list_line = list(line)
        grid.append(list_line)


rows, cols = len(grid), len(grid[0])  # This cols ref expects that all rows have the same length
numbers_found = []


def all_numbers_in_row_with_indices(row, lst):
    numbers_with_indices = []

    for index, element in enumerate(lst):
        if element.isdigit():
            numbers_with_indices.append((row, index, int(element)))

    print(f"Numbers with indices: {numbers_with_indices}")
    return numbers_with_indices


def get_numbers_with_symbol_hits() -> list:
    number_hits = []

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            number_hits = all_numbers_in_row_with_indices(row, grid[row][column])

    print(f"Number of hits: {number_hits}")
    return number_hits


def get_hits(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    hits = []

    # Horizontal and Vertical hits
    for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if 0 <= i < rows and 0 <= j < cols and matrix[i][j] in symbols:
            hits.append((i, j))

    # Diagonal hits
    for i, j in [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]:
        if 0 <= i < rows and 0 <= j < cols and matrix[i][j] in symbols:
            hits.append((i, j))

    return hits


def get_full_number(row, index):

    arr = grid[row]

    if 0 <= index < len(arr) and arr[index].isdigit():
        start, end = index, index

        # Expand to the left
        while start > 0 and arr[start - 1].isdigit():
            start -= 1

        # Expand to the right
        while end < len(arr) - 1 and arr[end + 1].isdigit():
            end += 1

        # Return the contiguous string of digits
        return int(''.join(arr[start:end + 1]))

    return None


last_number = None
for row, col in get_numbers_with_symbol_hits():
    for n_row, n_col in get_hits(grid, row, col):
        number = get_full_number(n_row, n_col)
        numbers_found.append(int(number))
        last_number = (n_row, n_col)


# print(sorted(get_all_neighbours(number_hits)))
print(numbers_found)
print(f"Sum of engine parts: {sum(numbers_found)}")
