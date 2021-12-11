import sys
import copy
import pathlib

import numpy as np


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        line_numbers = [int(energy) for energy in line]
        if len(line_numbers) > 0:
            data.append(line_numbers)
    return np.array(data, dtype=np.int8)


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    # parameters
    debug = False
    n_steps = 100

    n_flashes = 0
    energy_levels = copy.deepcopy(data)
    # start iteration process
    for n in range(n_steps):
        # constants
        U, V = energy_levels.shape

        # Create a map to keep track of if an octopus already flashed.
        flash_map = np.zeros_like(energy_levels, dtype=np.int8)

        while True:
            idu, idv = np.where(energy_levels >= 9)

            if len(idu) == 0:
                # increase the energy level of each octopus
                energy_levels += 1
                energy_levels[flash_map==1] = 0
                break

            # update flash map
            flash_map[idu, idv] = 1

            for u, v in zip(idu, idv):
                for du in range(-1, 1+1):
                    for dv in range(-1, 1+1):
                        i, j = u+du, v+dv
                        if 0 <= i < U and 0 <= j < V:
                            if flash_map[i, j] < 1:
                                energy_levels[i, j] += 1

            energy_levels[flash_map==1] = 0

        ids, _ = np.where(energy_levels == 0)

        n_flashes += len(ids)

        if debug:
            print(f'After step {n+1}:')
            print(energy_levels)

    return n_flashes


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1

    # parameters
    debug = False

    step = 0
    energy_levels = copy.deepcopy(data)
    # start iteration process
    while True:
        # constants
        U, V = energy_levels.shape
        # Create a map to keep track of if an octopus already flashed.
        flash_map = np.zeros_like(energy_levels, dtype=np.int8)

        while True:
            idu, idv = np.where(energy_levels >= 9)

            if len(idu) == 0:
                # increase the energy level of each octopus
                energy_levels += 1
                energy_levels[flash_map==1] = 0
                break

            # update flash map
            flash_map[idu, idv] = 1

            for u, v in zip(idu, idv):
                for du in range(-1, 1+1):
                    for dv in range(-1, 1+1):
                        i, j = u+du, v+dv
                        if 0 <= i < U and 0 <= j < V:
                            if flash_map[i, j] < 1:
                                energy_levels[i, j] += 1

            energy_levels[flash_map==1] = 0

        step += 1

        if debug:
            print(f'After step {step}:')
            print(energy_levels)

        # check if all energy levels at zero
        ids, _ = np.where(energy_levels == 0)
        if len(ids) == U * V:
            break

    return step


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

            print('Advent of Code 2021 - Day 11')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
