#!/usr/bin/env python
# -*- coding: utf-8 -*-

c_value_dict = {')':1, ']':2, '}':3, '>':4}

def open_typ(pos, line):
    err = 0
    cp = ''
    c = line[pos]
    p = pos
    if c == '(':
        err, p, cp = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p, cp = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p, cp = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p, cp = open_chunk_d(pos + 1, line)

    return err, p, cp


def open_chunk_a(pos, line):
    err = 0
    cp = ''
    c = line[pos]
    p = pos
    if c == '(':
        err, p, cp = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p, cp = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p, cp = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p, cp = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == ')' and p != 0:
        err, p, cp = open_typ(p + 1, line)
    elif c == ']':
        err = 57
        p = 0
    elif c == '}':
        err = 1197
        p = 0
    elif c == '>':
        err = 25137
        p = 0

    if c == '\n' and p != 0:
        cp += ')'

    return err, p, cp


def open_chunk_b(pos, line):
    err = 0
    cp = ''
    c = line[pos]
    p = pos
    if c == '(':
        err, p, cp = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p, cp = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p, cp = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p, cp = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == ']' and p != 0:
        err, p, cp = open_typ(p + 1, line)
    elif c == ')':
        err = 3
        p = 0
    elif c == '}':
        err = 1197
        p = 0
    elif c == '>':
        err = 25137
        p = 0

    if c == '\n' and p != 0:
        cp += ']'

    return err, p, cp


def open_chunk_c(pos, line):
    err = 0
    cp = ''
    c = line[pos]
    p = pos
    if c == '(':
        err, p, cp = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p, cp = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p, cp = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p, cp = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == '}' and p != 0:
        err, p, cp = open_typ(p + 1, line)
    elif c == ')':
        err = 3
        p = 0
    elif c == ']':
        err = 57
        p = 0
    elif c == '>':
        err = 25137
        p = 0

    if c == '\n' and p != 0:
        cp += '}'


    return err, p, cp


def open_chunk_d(pos, line):
    err = 0
    cp = ''
    c = line[pos]
    p = pos
    if c == '(':
        err, p, cp = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p, cp = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p, cp = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p, cp = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == '>' and p != 0:
        err, p, cp = open_typ(p + 1, line)
    elif c == ')':
        err = 3
        p = 0
    elif c == ']':
        err = 57
        p = 0
    elif c == '}':
        err = 1197
        p = 0

    if c == '\n' and p != 0:
        cp += '>'

    return err, p, cp


def calc_score(text):
    score = 0
    for c in text:
        score = (score * 5) + c_value_dict[c]
    return score


with open("input.txt", 'r') as fh:
    err = 0
    score_list = []
    for line in fh:
        c = line[0]
        if c == ')':
            err = 3
        elif c == ']':
            err = 57
        elif c == '}':
            err = 1197
        elif c == '>':
            err = 25137
        else:
            err, p, cp = open_typ(0, line)

        if err == 0:
            score_list.append(calc_score(cp))

    print(sorted(score_list)[int(len(score_list)/2)])
