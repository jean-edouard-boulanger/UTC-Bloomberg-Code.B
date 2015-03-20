#!/usr/bin/python

import sys

data = sys.stdin.readlines()
lines = data[1:]
grid = []
for line in lines:
    cells = [int(x) for x in line.split(" ")]
    grid.append(cells)

N = len(grid)

for y in reversed(range(0, N)):
    for x in reversed(range(0, N)):
        if x == y == (N - 1):
            continue

        min_cost = sys.maxint
        current_cell_cost = grid[y][x]

        if x < N - 1:
            hor_move_cost = current_cell_cost + grid[y][x + 1]

            if hor_move_cost < min_cost:
                min_cost = hor_move_cost

        if y < N - 1:
            ver_move_cost = current_cell_cost + grid[y + 1][x]
            if ver_move_cost < min_cost:
                min_cost = ver_move_cost

        grid[y][x] = min_cost

print grid[0][0]