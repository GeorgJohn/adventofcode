import sys
import pathlib

import numpy as np

y_id = 1
x_id = 0


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    commands = []
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            if 'fold along' in line:
                nose, tail = line.split('=')
                key = nose[-1]
                value = int(tail)
                commands.append((key, value))
            else:
                y, x = line.split(',')
                data.append((int(y), int(x)))
    return data, commands


def part1(data, commands, skip):
    """ Solve part 1 """
    if skip:
        return -1
    
    dots = np.array(data, dtype=np.int64)
    
    X, Y = np.max(dots, axis=0)

    paper = np.zeros([Y+1, X+1], dtype=np.int64)

    for dot in dots:
        paper[dot[y_id], dot[x_id]] = 1

    for command in commands:
        
        height, width = paper.shape

        if command[0] == 'y':
            new_paper = np.zeros([command[1], width], dtype=np.int64)
            h, w = new_paper.shape
            offset = 2 * h - height + 1
            # copy upper part
            new_paper[0:h, 0:w] = paper[0:h, 0:w]

            for fy, by in enumerate(range(height-1, h, -1)):
                for x in range(width):
                    value = paper[by, x]
                    if value == 1:
                        new_paper[fy + offset, x] = 1

        elif command[0] == 'x':
            new_paper = np.zeros([height, command[1]], dtype=np.int64)
            h, w = new_paper.shape
            offset = 2 * w - width + 1
            # copy left part
            new_paper[0:h, 0:w] = paper[0:h, 0:w]
            for y in range(height):
                for fx, bx in enumerate(range(width-1, w, -1)):
                    value = paper[y, bx]
                    if value == 1:
                        new_paper[y, fx+offset] = 1
        else:
            result = -1
            break

        break

    result = np.sum(new_paper)

    return result


def part2(data, commands, skip):
    """ Solve part 2 """
    if skip:
       return -1

    dots = np.array(data, dtype=np.int64)
    
    X, Y = np.max(dots, axis=0)

    paper = np.zeros([Y+1, X+1], dtype=np.int64)

    for dot in dots:
        paper[dot[y_id], dot[x_id]] = 1

    for command in commands:
        
        height, width = paper.shape

        if command[0] == 'y':
            new_paper = np.zeros([command[1], width], dtype=np.int64)
            h, w = new_paper.shape
            offset = 2 * h - height + 1
            # copy upper part
            new_paper[0:h, 0:w] = paper[0:h, 0:w]

            for fy, by in enumerate(range(height-1, h, -1)):
                for x in range(width):
                    value = paper[by, x]
                    if value == 1:
                        new_paper[fy + offset, x] = 1

        elif command[0] == 'x':
            new_paper = np.zeros([height, command[1]], dtype=np.int64)
            h, w = new_paper.shape
            offset = 2 * w - width + 1
            # copy left part
            new_paper[0:h, 0:w] = paper[0:h, 0:w]
            for y in range(height):
                for fx, bx in enumerate(range(width-1, w, -1)):
                    value = paper[y, bx]
                    if value == 1:
                        new_paper[y, fx+offset] = 1
        else:
            break

        paper = new_paper

    for line in paper:
        line_str = ''
        for num in line:
            if num == 0:
                c = '.'
            else:
                c = '#'
            line_str += c

        print(line_str)




def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data, puzzle_commands = parse(puzzle_input)
    
    solution1 = part1(puzzle_data, puzzle_commands, skip=False)
    part2(puzzle_data, puzzle_commands, skip=False)

    return [solution1]


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print(f'Please enter at least one file path.')
    else:
        for path in sys.argv[1:]:
            print(f'\n{path}:')
            puzzle_input = pathlib.Path(path).read_text().strip()

            print('Advent of Code 2021 - Day 12')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
