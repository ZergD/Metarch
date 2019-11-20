"""
Daily Coding Problem: Problem #2
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


# import itertools
#
# stuff = [1, 2, 3, 4]
# for L in range(0, len(stuff) + 1):
#     for subset in itertools.combinations(stuff, L):
#         print(subset)


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    #     # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        print("remLst = ", remLst)
        for p in permutation(remLst):
            print("we append [m] = {} + p = {}".format([m], p))
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for pp in permutation(data):
    print(pp)
print(len(permutation(data)))

# l = [1, 2, 3, 4, 5, 6]
#
# for i in range(1, 4):
#     print(i)
#     print(l[:i])
#     print(l[i:])
