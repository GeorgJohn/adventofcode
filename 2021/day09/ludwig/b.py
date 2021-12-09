#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def get_num_neighbours(h_map, j, i):
    n = {(j, i)}
    if h_map[j][i] < h_map[j-1][i]  < 9:
        n |= get_num_neighbours(h_map, j-1, i)
    if h_map[j][i] < h_map[j+1][i] < 9:
        n |= get_num_neighbours(h_map, j+1, i)
    if h_map[j][i] < h_map[j][i-1] < 9:
        n |= get_num_neighbours(h_map, j, i-1)
    if h_map[j][i] < h_map[j][i+1] < 9:
        n |= get_num_neighbours(h_map, j, i+1)
    return n


with open("input.txt", 'r') as fh:
    h_map = []
    for line in fh:
        h_map.append([9] + [int(c) for c in line[:-1]] + [9])

    x_max = len(h_map[0])
    h_map.insert(0, [9] * x_max)
    h_map.append([9] * x_max)
    y_max = len(h_map)
    low_points = []
    for i in range(1, x_max-1):
        for j in range(1, y_max-1):
            lvl = h_map[j][i]
            if lvl < h_map[j-1][i] and lvl < h_map[j+1][i] and lvl < h_map[j][i-1] and lvl < h_map[j][i+1]:
                low_points.append((j,i))

    basins = []
    for p in low_points:
        basins.append(len(get_num_neighbours(h_map, p[0], p[1])))

    print(np.prod(sorted(basins)[-3:]))
