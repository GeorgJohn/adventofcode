#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

with open("input.txt", 'r') as fh:
    line = fh.readline()
    pos = [int(x) for x in line.split(',')]
    a_pos = np.array(pos)
    align_pos = int(np.percentile(a_pos, 50))
    fuel = 0
    for p in pos:
        fuel += abs(p - align_pos)
    print(fuel)
