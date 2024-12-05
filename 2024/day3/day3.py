#!/usr/bin/env python3
import ast
import re

start = 0
search_pattern = r"mul\(\d+,\d+\)"

def mul(a, b):
    return a * b


functions = {'mul': mul}


with open("input.txt", "r") as f:
    data = f.read().splitlines()
    for line in data:
        vals = re.findall(search_pattern, line)
        for val in vals:
            func, args = val[:-1].split("(", 1)
            start += functions[func](*ast.literal_eval(args))

print(start)
