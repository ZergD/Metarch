from other import my_text
import os


def draf():
    print("File ex1.py accessed...")
    print(os)
    print("text = ", my_text)
    print("dirs = ", dir())


def solve(rules: dict):
    for key in rules.keys():
        print(rules[key])


# input_d = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
#
# solve(input_d)
#
# course_to_pre = {c: set(p) for c, p in input_d.items()}
#
# todo = [c for c, p in course_to_pre.items() if not p]
#
# res = {}
# for course in course_to_pre:
#     print(course)
#     print(course_to_pre[course])
#     for prereq in course_to_pre[course]:
#         if prereq not in res:
#             res[prereq] = []
#
#         res[prereq].append(course)
#
#     result = []
#
#     while todo:
#         prereq = todo.pop()
#         result.append(prereq)
