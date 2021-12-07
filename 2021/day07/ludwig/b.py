#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc_fuel(pos, pos_list):
    fuel = 0
    for p in pos_list:
        diff = abs(p - pos)
        fuel += 0.5 * (diff + 1) * diff
    return fuel


with open("input.txt", 'r') as fh:
    line = fh.readline()
    pos = [int(x) for x in line.split(',')]
    min_fuel = calc_fuel(1919, pos)
    for i in range(0, 1919):
        fuel = calc_fuel(i, pos)
        min_fuel = min(min_fuel, fuel)

    print(min_fuel)
