#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def simulate_step(octopuses):
    octopuses += 1
    flashed_this_step = []
    flashing = np.argwhere(octopuses > 9)
    for i in range(0, len(flashing)):
        simulate_flash(flashing[i], octopuses, flashed_this_step)
    octopuses[octopuses > 9] = 0
    return len(np.argwhere(octopuses == 0))


def simulate_flash(octopus, octopuses, flashed_this_step):
    if not index_in_list(octopus, flashed_this_step):
        flashed_this_step.append(octopus)
        for x in range(-1,2):
            for y in range(-1, 2):
                xi = octopus[0] + x
                yi = octopus[1] + y
                if xi >= 0 and xi < len(octopuses) and yi >= 0 and yi < len(octopuses):
                    octopuses[xi][yi] += 1
                    if octopuses[xi][yi] > 9:
                        simulate_flash([xi, yi], octopuses, flashed_this_step)


def index_in_list(idx, l):
    for i in l:
        if i[0] == idx[0] and i[1] == idx[1]:
            return True
    return False


with open("input.txt", 'r') as fh:
    octopuses = []
    for line in fh:
        octopuses.append([int(c) for c in line[:-1]])

    octopuses = np.array(octopuses)
    all = octopuses.size
    steps = 0
    while True:
        flashes = simulate_step(octopuses)
        steps += 1
        if flashes == all:
            print(steps)
            break
