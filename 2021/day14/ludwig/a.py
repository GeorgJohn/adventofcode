#!/usr/bin/env python
# -*- coding: utf-8 -*-


def update_polymer(seq, rules):
    copy = seq
    pos = 1
    for i in range(0, len(seq)-1):
        if seq[i:i+2] in rules:
            copy = copy[:pos] + rules[seq[i:i+2]] + copy[pos:]
            pos += 2
        else:
            pos += 1
            print(seq[i:i+2])

    return copy

with open("input.txt", 'r') as fh:
    seq = ''
    rules = {}
    for i, line in enumerate(fh):
        if i == 0:
            seq = line[:-1]
        elif i > 1:
            pattern = line.split(' ')[0]
            char = line.split(' ')[2][:-1]
            rules[pattern] = char

    for i in range(0, 10):
        seq = update_polymer(seq, rules)

    unique_char = set(seq)
    char_count = []
    for char in unique_char:
        char_count.append(seq.count(char))
    print(max(char_count) - min(char_count))

