#!/usr/bin/python

import sys


def is_prime(mx):
    for d in range(2, mx):
        if mx % d == 0:
            return False
    return True


def largest_twin_primes(ubound):
    for x in reversed(range(3, ubound + 1)):
        if is_prime(x) and is_prime(x - 2):
            return str(x - 2) + "," + str(x)


K = int(sys.stdin.readline())
print(largest_twin_primes(K))