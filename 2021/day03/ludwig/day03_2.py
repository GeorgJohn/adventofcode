#!/usr/bin/env python
# -*- coding: utf-8 -*-


def most_common_bit_1(pos, numbers):
    one_count = 0
    zero_count = 0
    for n in numbers:
        if (n & (1 << pos)) != 0:
            one_count += 1
        else:
            zero_count += 1

    return one_count >= zero_count


with open("input.txt", 'r') as fh:
    numbers = []

    for line in fh:
        numbers.append(int(line, 2))

    oxygen = numbers
    CO2 = numbers
    for pos in range(11, -1, -1):
        if len(oxygen) != 1:
            if most_common_bit_1(pos, oxygen):
                f = filter(lambda x: (x & (1 << pos)) != 0, oxygen)
                oxygen = list(f)
            else:
                f = filter(lambda x: (x & (1 << pos)) == 0, oxygen)
                oxygen = list(f)
        if len(CO2) != 1:
            if most_common_bit_1(pos, CO2):
                f = filter(lambda x: (x & (1 << pos)) == 0, CO2)
                CO2 = list(f)
            else:
                f = filter(lambda x: (x & (1 << pos)) != 0, CO2)
                CO2 = list(f)

    print(oxygen[0] * CO2[0])
