#!/usr/bin/env python
# -*- coding: utf-8 -*-


def draw_line(line, field, x_max):
    if line[1] == line[3]:
        draw_horizontal_line(line, field, x_max)
    elif line[0] == line[2]:
        draw_vertical_line(line, field, x_max)


def draw_vertical_line(line, field, x_max):
    x = line[0]
    if line[1] < line[3]:
        r = range(line[1], line[3] + 1)
    else:
        r = range(line[3], line[1] + 1)
    for i in r:
        field[x + (x_max * i)] += 1


def draw_horizontal_line(line, field, x_max):
    y = line[1]
    if line[0] < line[2]:
        r = range(line[0], line[2] + 1)
    else:
        r = range(line[2], line[0] + 1)
    for i in r:
        field[(y * x_max) + i] += 1


def count_overlap(field):
    count = 0
    for p in field:
        if p > 1:
            count += 1
    return count


def print_field(field, x_max, y_max):
    with open('debug.txt', 'w') as fh:
        for y in range(0, y_max):
            line = ''
            for x in range(0, x_max):
                if field[y * x_max + x] == 0:
                    line += '.'
                else:
                    line += str(field[y * x_max + x])
            fh.write(line + '\n')


lines2draw = []

with open("input.txt", 'r') as fh:
    x_max = 0
    y_max = 0
    for l in fh:
        s = l.split(' ')
        x1 = int(s[0].split(',')[0])
        x_max = max(x1, x_max)
        y1 = int(s[0].split(',')[1])
        y_max = max(y1, y_max)
        x2 = int(s[2].split(',')[0])
        x_max = max(x2, x_max)
        y2 = int(s[2].split(',')[1])
        y_max = max(y2, y_max)
        if (x1 == x2) or (y1 == y2):
            lines2draw.append((x1, y1, x2, y2))
        x_max += 1
        y_max += 1

    field = [0] * (x_max * y_max)
    for line in lines2draw:
        draw_line(line, field, x_max)
    print(count_overlap(field))
    print_field(field, x_max, y_max)
