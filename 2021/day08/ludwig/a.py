#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("input.txt", 'r') as fh:
    count = 0
    for line in fh:
        output = line.split('|')[1].strip().split(' ')
        for digit in output:
            length = len(digit)
            if length == 2 or length == 3 or length == 4 or length == 7:
                count += 1

    print(count)
