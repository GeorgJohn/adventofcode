#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
paper = np.zeros((1311, 895), dtype=int)

fold_instructions = []


def fold_along_x(paper, pos):
    x_max = paper.shape[0]
    for i, j in zip(range(pos+1, x_max), range(pos-1, -1, -1)):
        paper[j] += paper[i]

    return paper[0:pos]


def fold_along_y(paper, pos):
    y_max = paper.shape[1]
    for i, j in zip(range(pos+1, y_max), range(pos-1, -1, -1)):
        paper[:,j] += paper[:,i]

    return paper[:,0:pos]


with open("input.txt", 'r') as fh:
    read_folds = False
    for line in fh:
        if read_folds:
            inst = line.split(' ')[2]
            direction = inst.split('=')[0]
            position = int(inst.split('=')[1][:-1])
            fold_instructions.append((direction, position))
        else:
            if line != '\n':
                x = int(line.split(',')[0])
                y = int(line.split(',')[1][:-1])
                paper[x][y] = 1
            else:
                read_folds = True

    for inst in fold_instructions:
        if inst[0] == 'x':
            paper = fold_along_x(paper, inst[1])
        else:
            paper = fold_along_y(paper, inst[1])
    print(paper)
