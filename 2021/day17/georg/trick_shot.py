import re
from sre_constants import BRANCH
import sys
import pathlib


def parse(puzzle_input):
    """ Parse text input in data array. """
    data = []
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            
            match_x = line.find('x=')
            match_y = line.find('y=')
            # cut out important string area
            x_values = line[match_x+2:match_y-2]
            y_values = line[match_y+2:]

            x_digits = tuple([int(digit) for digit in x_values.split('..')])
            y_digits = tuple([int(digit) for digit in y_values.split('..')])

            data = [x_digits, y_digits]
    return data


def step(xy, dxy):

    xy[0] = xy[0] + dxy[0]
    xy[1] = xy[1] + dxy[1]

    if dxy[0] > 0: dxy[0] -= 1
    elif dxy[0] < 0: dxy[0] += 1
    else: dxy[0] = 0 
    # gravity term
    dxy[1] -= 1
    return xy, dxy


def part1(data, skip):
    """ Solve part 1 """
    if skip:
       return -1

    tgt_xx = data[0]
    tgt_yy = data[1]

    xy = [0, 0]
    dxy = [6, 9]

    global_heighest_y = 0

    for dx in range(0, tgt_xx[1] + 1):
        for dy in range(tgt_yy[0]-1, 500):
            
            xy = [0, 0]
            dxy = [dx, dy]

            match_tgt = False
            tmp_heighest_y = 0
            while True:
                
                xy, dxy = step(xy, dxy)

                if xy[1] > tmp_heighest_y:
                    tmp_heighest_y = xy[1]

                if tgt_xx[0] <= xy[0] <= tgt_xx[1] and tgt_yy[0] <= xy[1] <= tgt_yy[1]:
                    match_tgt = True
                    break

                if xy[0] > tgt_xx[1] or xy[1] < tgt_yy[0]:
                    break

            if match_tgt:
                if tmp_heighest_y > global_heighest_y:
                    global_heighest_y = tmp_heighest_y

    return global_heighest_y


def part2(data, skip):
    """ Solve part 2 """
    if skip:
        return -1

    tgt_xx = data[0]
    tgt_yy = data[1]

    match_count = 0

    for dx in range(0, tgt_xx[1] + 1):
        for dy in range(tgt_yy[0]-1, 500):
            
            xy = [0, 0]
            dxy = [dx, dy]

            match_tgt = False
            while True:
                
                xy, dxy = step(xy, dxy)

                if tgt_xx[0] <= xy[0] <= tgt_xx[1] and tgt_yy[0] <= xy[1] <= tgt_yy[1]:
                    match_tgt = True
                    break

                if xy[0] > tgt_xx[1] or xy[1] < tgt_yy[0]:
                    break

            if match_tgt:
                match_count += 1

    return match_count


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)

    solution1 = part1(puzzle_data, skip=False)
    solution2 = part2(puzzle_data, skip=False)

    return solution1, solution2


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print(f'Please enter at least one file path.')
    else:
        for path in sys.argv[1:]:
            print(f'\n{path}:')
            puzzle_input = pathlib.Path(path).read_text().strip()

            print('Advent of Code 2021 - Day 17')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
