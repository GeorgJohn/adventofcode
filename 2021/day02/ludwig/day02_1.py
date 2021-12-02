#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input_1.txt", 'r') as fh:
    pos = 0
    depth = 0
    for line in fh:
        if line.startswith('forward'):
            pos += int(line.split(' ')[1])
        elif line.startswith('down'):
            depth += int(line.split(' ')[1])
        elif line.startswith('up'):
            depth -= int(line.split(' ')[1])
        else:
            print('error')
        print(line, pos, depth)

    print(pos * depth)
