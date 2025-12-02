#!/usr/bin/env python3
import re


def get_columns(data):
    columns = []
    for i in range(len(data[0])):
        column = ''
        for j in range(len(data)):
            column += data[j][i]
        columns.append(column)
    return columns


def get_diagonals_ltr(data):
    diagonals = []
    # for each line/item in data
    for i in range(len(data)):
        # for each character in the line
        for j in range(len(data[i])):
            # if we are at the start of the line or the start of the item
            if i == 0 or j == 0:
                diagonal_ltr = ''
                while i < len(data) and j < len(data[i]):
                    diagonal_ltr += data[i][j]
                    i += 1
                    j += 1
                if len(diagonal_ltr) >= 4:
                    diagonals.append(diagonal_ltr)
    return diagonals


def get_diagonals_rtl(data):
    diagonals = []
    # for each line/item in data
    for i in range(len(data)):
        # for each character in the line
        for j in range(len(data[i])):
            # if we are at the start of the line or the end of the item
            if i == 0 or j == len(data[i]) - 1:
                diagonal_rtl = ''
                while i < len(data) and j >= 0:
                    diagonal_rtl += data[i][j]
                    i += 1
                    j -= 1
                if len(diagonal_rtl) >= 4:
                    diagonals.append(diagonal_rtl)
    return diagonals


def add_matches_to_count(data, count):
    for line in data:
        # matches = re.finditer('(?=(XMAS|SAMX))', line)
        # count += len([match.group(1) for match in matches])
        count += len(re.findall('XMAS|SAMX', line))
    return count


count = 0
with open('input.txt') as f:
    data = f.read().splitlines()
    count += add_matches_to_count(data, count)
    count += add_matches_to_count(get_columns(data), count)
    count += add_matches_to_count(get_diagonals_ltr(data), count)
    count += add_matches_to_count(get_diagonals_rtl(data), count)
    print(get_diagonals_ltr(data))
    print(get_diagonals_rtl(data))

print(count)


# 3074 is wrong; too high
# 1317 is wrong; too low
