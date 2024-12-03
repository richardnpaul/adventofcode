#!/usr/bin/env python3


def incdec_test(array):
    return (
        all(0 <= array[i+1] - array[i] <= 3 for i in range(len(array) - 1)) or
        all(0 <= array[i] - array[i+1] <= 3 for i in range(len(array) - 1))
    )


def check_safe_unsafe():
    list_of_lists = []
    num_safe = 0
    num_unsafe = 0

    with open("input.txt") as f:
        for line in f:
            stripped_line = line.rstrip("\n")
            list_of_lists.append([int(i) for i in stripped_line.split(" ")])

    for l in list_of_lists:
        if incdec_test(l):
            print(l)
            num_safe += 1
        else:
            num_unsafe += 1
    print(f"Safe: {num_safe}, Unsafe: {num_unsafe}")

if __name__ == "__main__":
    check_safe_unsafe()
