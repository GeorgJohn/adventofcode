#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_mapping(data):
    mapping = []
    data_sets = {}
    for d in data:
        if len(d) == 2:
            mapping.append((d, '1'))
            data_sets[1] = set(d)
        elif len(d) == 3:
            mapping.append((d, '7'))
            data_sets[7] = set(d)
        elif len(d) == 4:
            mapping.append((d, '4'))
            data_sets[4] = set(d)
        elif len(d) == 7:
            mapping.append((d, '8'))
            data_sets[8] = set(d)

    for d in data:
        if len(d) == 6 and data_sets[4].issubset(set(d)):
            mapping.append((d, '9'))
        elif len(d) == 5 and data_sets[1].issubset(set(d)):
            mapping.append((d, '3'))
        elif len(d) == 5 and (data_sets[8] - data_sets[4]).issubset(set(d)):
            mapping.append((d, '2'))
        elif len(d) == 6 and len(set(d)-data_sets[1]) == 4:
            mapping.append((d, '0'))
        elif len(d) == 6 and len(set(d)-data_sets[1]) == 5:
            mapping.append((d, '6'))
        elif len(d) == 5:
            mapping.append((d, '5'))
    return mapping


def get_digit(mapping, pattern):
    for m in mapping:
        if set(m[0]) == set(pattern):
            return m[1]
    print(mapping, pattern)


with open("input.txt", 'r') as fh:
    count = 0
    for line in fh:
        data = line.split('|')[0].strip().split(' ')
        output = line.split('|')[1].strip().split(' ')
        mapping = get_mapping(data)
        num = ''
        for digit in output:
            num += get_digit(mapping, digit)
        count += int(num)

    print(count)
