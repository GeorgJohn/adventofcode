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

    # expand_positions = []
    
    # for position in data:
    #     exp_pos = 0
    #     for n in range(position):
    #         exp_pos += 1 * (n+1)

    #     expand_positions.append(exp_pos)
    
    # median = round(np.median(expand_positions))

  
    # print(sorted(expand_positions))
    # print(median)
    
    lowest_fuel = np.inf
    lowest_fuel_idx = 0

    for median in range(0, 1000):

        expand_positions = []
        
        for position in data:
            exp_pos = 0
            for n in range(abs(position - median)):
                exp_pos += 1 * (n+1)

            expand_positions.append(exp_pos)
        
        fuel = np.sum(expand_positions)

        if fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_idx = median

    print(lowest_fuel_idx)
    return lowest_fuel


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)
    
    # print list - line by line
    # print('\n'.join(str(line) for line in puzzle_data))

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
