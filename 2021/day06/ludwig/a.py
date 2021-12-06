#!/usr/bin/env python
# -*- coding: utf-8 -*-


def num_fish(offset, days):
    fish = 1
    for i in range(offset, days+1, 7):
        fish += num_fish(i + 9, days)
    return fish


lanternfish = []

with open("input.txt", 'r') as fh:
    line = fh.readline()
    lanternfish = [int(x) for x in line.split(',')]
    count = 0
    for i in lanternfish:
        count += num_fish(i+1, 80)

    print(count)
