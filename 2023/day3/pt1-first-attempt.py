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

ignore_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '.']
symbols = [i for i in sorted_list if i not in ignore_list]

grid = []

with open(argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        list_line = list(line)
        grid.append(list_line)


rows, cols = len(grid), len(grid[0])  # This cols ref expects that all rows have the same length
numbers_found = []


def all_numbers_in_row_with_indices(row: int, lst: list) -> list:
    numbers_with_indices = []

    for index, element in enumerate(lst):
        if element.isdigit():
            numbers_with_indices.append((row, index, int(element)))

    return numbers_with_indices


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


def get_numbers_with_symbol_hits(row: list) -> list:
    number_hits = []
    numbers_next_to_symbols = []

    number_hits = all_numbers_in_row_with_indices(grid.index(row), row)
    for hit in number_hits:
        numbers_next_to_symbols.append(get_hits(grid, hit[0], hit[1]))

    return numbers_next_to_symbols


def get_full_number(row: list, index: int) -> None or int:

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
for row in grid:
    hits = get_numbers_with_symbol_hits(row)
    for hit in hits:
        number = get_full_number(hit[0], hit[1])
        if number:
            numbers_found.append(int(number))
        last_number = (hit[0], hit[1])


# print(sorted(get_all_neighbours(number_hits)))
print(numbers_found)
print(f"Sum of engine parts: {sum(numbers_found)}")
