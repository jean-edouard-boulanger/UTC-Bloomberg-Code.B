#!/usr/bin/python

import sys


def is_palindrome(word):
    return word == reverse(word)


def reverse(word):
    return word[::-1]

data = sys.stdin.readlines()
N = int(data[0])
gloves = [x.rstrip() for x in data[1:]]

gloves_count = dict()

for glove_name in gloves:

    if is_palindrome(glove_name):
        continue

    key = glove_name
    if key not in gloves_count:
        key = reverse(glove_name)

    if key not in gloves_count:
        gloves_count[key] = 1
    else:
        gloves_count[key] += 1


total_pair_gloves = 0
for k, v in gloves_count.items():
    if v % 2 > 0:
        total_pair_gloves = -1
        break
    total_pair_gloves += v / 2

print total_pair_gloves