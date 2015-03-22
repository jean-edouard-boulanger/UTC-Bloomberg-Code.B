#!/usr/bin/python

import sys


def count_books_to_read(friends, source, books, max_separation_degree):
    explored = []
    books_to_read = []
    books_already_read = []

    to_explore = [source]
    to_explore_count = 1
    current_degree = 0

    if source in books:
        books_already_read += books[source]

    while len(to_explore) > 0 and current_degree <= max_separation_degree:

        current_person = to_explore.pop()
        if current_person in friends:
            current_person_friends = friends[current_person]
            for friend in current_person_friends:
                if friend not in explored:
                    to_explore.insert(0, friend)

        if current_person in books:
            current_person_books = books[current_person]
            for book in current_person_books:
                if book not in books_already_read and book not in books_to_read:
                    books_to_read.append(book)

        to_explore_count -= 1
        if to_explore_count == 0:
            current_degree += 1
            to_explore_count = len(to_explore)

    return len(books_to_read)



data = sys.stdin.readlines()

source = data[0].rstrip()
max_separation_degree = int(data[1].rstrip())
links_count = int(data[2].rstrip())
book_lists_count = int(data[3].rstrip())

friends = dict()
links = [link.rstrip() for link in data[4:4 + links_count]]

first_book_idx = 4 + links_count
books_read = [book.rstrip() for book in data[first_book_idx:first_book_idx + book_lists_count]]

for link in links:
    real_link = link.split("|")
    p1 = real_link[0]
    p2 = real_link[1]
    if p1 not in friends:
        friends[p1] = []
    friends[p1].append(p2)

books = dict()
for book_link in books_read:
    real_book_link = book_link.split("|")
    p = real_book_link[0]
    books[p] = real_book_link[1:]


print count_books_to_read(friends, source, books, max_separation_degree)