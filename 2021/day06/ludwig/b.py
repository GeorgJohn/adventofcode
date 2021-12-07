#!/usr/bin/env python
# -*- coding: utf-8 -*-

new_fish = [0] * (256+8)


def num_fish(days):
    if new_fish[days] != 0:
        return new_fish[days]
    else:
        count = 1
        if days >= 9:
            for i in range(0, days-9+1, 7):
                count += num_fish(days-9-i)
        new_fish[days] = count
        return count

with open("input.txt", 'r') as fh:
    line = fh.readline()
    lanternfish = [int(x) for x in line.split(',')]
    total = 0
    for f in lanternfish:
        total += num_fish(256+8-f)
    print(total)
