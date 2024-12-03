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
# .11+.+11..

import re

def file_input_to_list_of_strings(file_name: str) -> list:
    """Takes in a file name and returns a matrix of lists of lists of characters for each line in
    the file"""
    with open(file_name, 'r') as f:
        return [str(line.rstrip()) for line in f.readlines()]


def get_symbols(list_of_strings):
    ignore_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    symbols = [c for string in list_of_strings for c in string if c not in ignore_list]
    return sorted(set(symbols))


def main():
    input_file = 'input.txt'
    str_list: list(str) = file_input_to_list_of_strings(input_file)
    symbols: list(str) = get_symbols(str_list)
    numbers: list(str) = [re.findall(r'\d+', ''.join(row)) for row in str_list]
    all_matches = []
    match_list = []

    for index, number_row in enumerate(numbers):
        print(f"index: {index}")
        for number in number_row:
            m = re.finditer(number, str_list[index])
            for match in m:
                if any(i for i in match_list if match.span() == i.span() and match.group() == i.group()):
                    continue
                match_list.append(match)
                start = match.start() - 1 if match.start() - 1 >= 0 else match.start()
                end = match.end() if match.end() + 1 == len(str_list[index]) else match.end() + 1
                subset_list = [
                    str_list[index - 1][start:end] if index - 1 >= 0 else "",
                    str_list[index][start:end],
                    "" if index + 1 == len(str_list) else str_list[index + 1][start:end]
                ]
                # print(subset_list)
                if any(symbol in ''.join(subset_list) for symbol in symbols):
                    print(f'match string = {"".join(subset_list)}')
                    all_matches.append(int(number))

    # for match in match_list: print(match)
    return print(sum(all_matches))

main()
