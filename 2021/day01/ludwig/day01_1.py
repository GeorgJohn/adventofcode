#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input_1.txt", 'r') as fh:
    prev = None
    inc_count = 0
    for l in fh:
        if prev is not None:
            n = int(l)
            if n > prev:
                inc_count += 1
            prev = n
        else:
            prev = int(l)

    print(inc_count)
