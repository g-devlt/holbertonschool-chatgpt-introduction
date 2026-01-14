#!/usr/bin/python3
import sys

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    while n > 1:
        result *= n
        n -= 1

    return result

f = factorial(int(sys.argv[1]))
print(f)