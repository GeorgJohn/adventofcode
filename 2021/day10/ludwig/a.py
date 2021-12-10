#!/usr/bin/env python
# -*- coding: utf-8 -*-


def open_typ(pos, line):
    err = 0
    c = line[pos]
    p = pos
    if c == '(':
        err, p = open_chunk_a(pos+1, line)
    elif c == '[':
        err, p = open_chunk_b(pos+1, line)
    elif c == '{':
        err, p = open_chunk_c(pos+1, line)
    elif c == '<':
        err, p = open_chunk_d(pos+1, line)

    return err, p


def open_chunk_a(pos, line):
    err = 0
    c = line[pos]
    p = pos
    if c == '(':
        err, p = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == ')' and p != 0:
        err, p = open_typ(p + 1, line)
    elif c == ']':
        err = 57
        p = 0
    elif c == '}':
        err = 1197
        p = 0
    elif c == '>':
        err = 25137
        p = 0

    return err, p


def open_chunk_b(pos, line):
    err = 0
    c = line[pos]
    p = pos
    if c == '(':
        err, p = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == ']' and p != 0:
        err, p = open_typ(p + 1, line)
    elif c == ')':
        err = 3
        p = 0
    elif c == '}':
        err = 1197
        p = 0
    elif c == '>':
        err = 25137
        p = 0

    return err, p


def open_chunk_c(pos, line):
    error_score = 0
    c = line[pos]
    p = pos
    if c == '(':
        error_score, p = open_chunk_a(pos + 1, line)
    elif c == '[':
        error_score, p = open_chunk_b(pos + 1, line)
    elif c == '{':
        error_score, p = open_chunk_c(pos + 1, line)
    elif c == '<':
        error_score, p = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == '}' and p != 0:
        error_score, p = open_typ(p + 1, line)
    elif c == ')':
        error_score = 3
        p = 0
    elif c == ']':
        error_score = 57
        p = 0
    elif c == '>':
        error_score = 25137
        p = 0

    return error_score, p


def open_chunk_d(pos, line):
    err = 0
    c = line[pos]
    p = pos
    if c == '(':
        err, p = open_chunk_a(pos + 1, line)
    elif c == '[':
        err, p = open_chunk_b(pos + 1, line)
    elif c == '{':
        err, p = open_chunk_c(pos + 1, line)
    elif c == '<':
        err, p = open_chunk_d(pos + 1, line)
    c = line[p]
    if c == '>' and p != 0:
        err, p = open_typ(p + 1, line)
    elif c == ')':
        err = 3
        p = 0
    elif c == ']':
        err = 57
        p = 0
    elif c == '}':
        err = 1197
        p = 0

    return err, p


with open("input.txt", 'r') as fh:
    error_score = 0
    for line in fh:
        c = line[0]
        if c == ')':
            error_score += 3
        elif c == ']':
            error_score += 57
        elif c == '}':
            error_score += 1197
        elif c == '>':
            error_score += 25137
        else:
            err, p = open_typ(0, line)
            error_score += err

    print(error_score)