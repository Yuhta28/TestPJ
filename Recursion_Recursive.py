#!/usr/bin/env python
import sys

sys.setrecursionlimit(5000)

# Recursion
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        print(len(list))
        return list[0] + sum(list[1:])

print(sum([5,7,3,8,10]))

print("")

# Factorial with recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

print("")

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

print(factorial2(3000))