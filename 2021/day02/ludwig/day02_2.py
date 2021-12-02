#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input_2.txt", 'r') as fh:
    pos = 0
    depth = 0
    aim = 0
    for line in fh:
        value = int(line.split(' ')[1])
        if line.startswith('forward'):
            pos += value
            depth += aim * value
        elif line.startswith('down'):
            aim += value
        elif line.startswith('up'):
            aim -= value
        else:
            print('error')
        print(line, pos, depth, aim)

    print(pos * depth)