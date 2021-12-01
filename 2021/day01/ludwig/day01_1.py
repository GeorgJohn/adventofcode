#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", 'r') as fh:
    prev = None
    inc_count = 0
    for l in fh:
        if prev != None:
            next = int(l)
            if next > prev:
                inc_count += 1
            prev = next
        else:
            prev = int(l)


    print(inc_count)
