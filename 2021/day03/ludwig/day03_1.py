#!/usr/bin/env python
# -*- coding: utf-8 -*-

one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("input.txt", 'r') as fh:
    for line in fh:
        for i in range(0, 12):
            if line[i] == '1':
                one_count[i] += 1
            else:
                zero_count[i] += 1

    gamma_str = ''
    epsilon_str = ''

    for i in range(0, 12):
        if one_count[i] >= zero_count[i]:
            gamma_str += '1'
            epsilon_str += '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'

    print(int(gamma_str, 2) * int(epsilon_str, 2))
