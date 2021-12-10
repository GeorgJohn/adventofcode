#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", 'r') as fh:
    h_map = []
    for line in fh:
        h_map.append([9] + [int(c) for c in line[:-1]] + [9])

    x_max = len(h_map[0])
    h_map.insert(0, [9] * x_max)
    h_map.append([9] * x_max)
    y_max = len(h_map)
    risk_lvl = 0
    for i in range(1, x_max-1):
        for j in range(1, y_max-1):
            lvl = h_map[j][i]
            if lvl < h_map[j-1][i] and lvl < h_map[j+1][i] and lvl < h_map[j][i-1] and lvl < h_map[j][i+1]:
                risk_lvl += lvl + 1

    print(risk_lvl)

