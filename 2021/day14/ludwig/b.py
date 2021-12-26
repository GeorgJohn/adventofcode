#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_char_count(rules_count_lut, pattern, steps, max_steps):
    remaining = max_steps - steps
    return rules_count_lut[remaining][pattern]


def update_count(a, b):
    for k in a.keys():
        a[k] += b[k]


def get_insert_char(a, b, rules):
    return rules[a + b]


def update_polymer(a, b, char_count, rules, steps, max_steps, rules_count_lut, empty_char_count):
    if steps < max_steps:
        existing_char_count = get_char_count(rules_count_lut, a + b, steps, max_steps)
        if existing_char_count:
            update_count(char_count, existing_char_count)
        else:
            insert_char = get_insert_char(a, b, rules)
            new_char_count = dict(empty_char_count)
            new_char_count[insert_char] += 1
            update_polymer(a, insert_char, new_char_count, rules, steps + 1, max_steps, rules_count_lut, empty_char_count)
            update_polymer(insert_char, b, new_char_count, rules, steps + 1, max_steps, rules_count_lut, empty_char_count)
            rules_count_lut[max_steps - steps][a+b] = new_char_count
            update_count(char_count, new_char_count)


with open("input.txt", 'r') as fh:
    seq = ''
    replace_pattern = {}
    unique_char = set()
    for i, line in enumerate(fh):
        if i == 0:
            seq = line[:-1]
        elif i > 1:
            pattern = line.split(' ')[0]
            char = line.split(' ')[2][:-1]
            replace_pattern[pattern] = char
            unique_char.add(char)

    empty_char_count = {}
    for c in unique_char:
        empty_char_count[c] = 0
    empty_rules_char_count = {}
    for i in replace_pattern.keys():
        empty_rules_char_count[i] = None

    rules_lut = [dict(empty_rules_char_count) for i in range(0, 41)]

    char_count = {}
    for char in unique_char:
        char_count[char] = seq.count(char)

    for i in range(0, len(seq)-1):
        update_polymer(seq[i], seq[i+1], char_count, replace_pattern, 0, 40, rules_lut, empty_char_count)

    print(max(char_count.values()) - min(char_count.values()))