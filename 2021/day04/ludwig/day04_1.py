#!/usr/bin/env python
# -*- coding: utf-8 -*-


def update_hits(num, board, board_hits):
    if num in board:
        idx = board.index(num)
        row = idx % 5
        col = int(idx / 5)
        board_hits[0][row] += 1
        if board_hits[0][row] == 5:
            return True
        board_hits[1][col] += 1
        if board_hits[1][col] == 5:
            return True
        return False


sequence = []
boards = []
board_hit_list = []

with open("input.txt", 'r') as fh:
    new_board = []
    for i, line in enumerate(fh):
        if i == 0:
            sequence = [int(n) for n in line.split(',')]
        elif i > 1:
            if line == '\n':
                boards.append(new_board)
                board_hit_list.append(([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
                new_board = []
            else:
                new_board.extend([int(n) for n in line.split()])

    draws = []
    for n in sequence:
        draws.append(n)
        for b, h in zip(boards, board_hit_list):
            if update_hits(n, b, h):
                print('bingo')
                print(sum(list(set(b) - set(draws))) * n)
                break
        else:
            continue
        break
