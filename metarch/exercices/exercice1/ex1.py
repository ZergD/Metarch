# from other import my_text
import os

"""
Daily Coding Problem: Problem #1
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

# def draf():
#     print("File ex1.py accessed...")
#     print(os)
#     print("text = ", my_text)
#     print("dirs = ", dir())


def solve(l: list, n: int):
    for i, a in enumerate(l):
        for b in l[i+1:]:
            if a + b == n:
                print(a, b)
                return True, [a, b]
    return False


# input = [10, 15, 3, 7]

# print("IMPORT POWER result = ", solve(input, 17))

