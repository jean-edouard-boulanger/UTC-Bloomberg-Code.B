#!/usr/bin/python

import sys

data = sys.stdin.readlines()
words = data[1:]

word_length = len(words[0]) - 1
result_word = ""

for i in range(0, word_length):
    letter_count = dict()
    for word in words:
        letter = word[i]
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    result_word += max(letter_count, key=letter_count.get)

print(result_word)