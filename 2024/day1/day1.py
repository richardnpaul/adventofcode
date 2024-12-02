#!/usr/bin/env python3

def sorted_list(input_file):
    dp1 = []
    dp2 = []
    with open(input_file) as f:
        for line in f:
            dp1.append(int(line.split(",")[0]))
            dp2.append(int(line.split(",")[1]))
    return zip(sorted(dp1), sorted(dp2))


def part1():
    distances = []
    for i, j in sorted_list("input.txt"):
        distances.append(abs(i - j))
    print(sum(distances))


if __name__ == "__main__":
    part1()
