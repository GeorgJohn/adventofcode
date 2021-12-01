#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input_2.txt", 'r') as fh:
    inc_count = 0
    inputs = []
    for l in fh:
        inputs.append(int(l))

    windows = []
    for i in range(0,len(inputs)-len(inputs)%3):
        windows.append(inputs[i] + inputs[i+1] + inputs[i+2])

    prev = None
    for w in windows:
        if prev is not None:
            if w > prev:
                inc_count += 1
            prev = w
        else:
            prev = w
    print(inc_count)