import sys
import pathlib

import numpy as np
from numpy.lib.function_base import median


def parse(puzzle_input):
    """ Parse text input in data array. """
    return [int(digit) for digit in puzzle_input.split(',')]


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return 0

    positions = np.array(data)
    median = round(np.median(positions))
    fuel = np.sum(np.abs(positions - median))

    return fuel


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return 0

    fuels = []
    max_pos = max(data)
    for align_pos in range(0, max_pos):
        costs = []
        for position in data:
            diff = abs(position - align_pos)
            cost = (diff ** 2 + diff) // 2  # small Gauss
            costs.append(cost)
        fuels.append(sum(costs))

    return min(fuels)


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

            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
