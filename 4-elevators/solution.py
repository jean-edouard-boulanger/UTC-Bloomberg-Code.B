#!/usr/bin/python

import sys


data = sys.stdin.readlines()

top_floor_number = int(data[0])
elevators = data[2:]

for i in range(0, len(elevators)):
    elevators[i] = [int(x) for x in elevators[i].split()]

reachable_floors = dict()
for elevator in elevators:
    for floor in elevator:
        if floor not in reachable_floors:
            reachable_floors[floor] = []
        reachable_floors[floor] += elevator
        reachable_floors[floor].remove(floor)

to_explore = [0]
to_explore_count = 1
depth = 0

explored = []
rides_count = 0
while len(to_explore) > 0:

    current_floor = to_explore.pop()

    if current_floor == top_floor_number:
        print str(depth)
        break

    next_floors = reachable_floors[current_floor]
    for floor in next_floors:
        if floor not in explored and floor not in to_explore:
            to_explore.insert(0, floor)

    explored += [current_floor]
    to_explore_count -= 1
    if to_explore_count == 0:
        to_explore_count = len(to_explore)
        depth += 1