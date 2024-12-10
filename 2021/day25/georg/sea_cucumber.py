import sys
import pathlib
import numpy as np
from numpy.core.records import array


REP2NUM_DICT = {
    '.': 0,
    '>': 1,
    'v': 2,
}

NUM2REP_DICT = {value:key for key, value in REP2NUM_DICT.items()}


def parse(puzzle_input):
    """ Parse text input in data array. """
    data = []
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            data_line = [REP2NUM_DICT[entry] for entry in line]
            data.append(data_line)
    return np.array(data, dtype=np.int32)


def print_map(data_array):
    R, C = data_array.shape
    for r in range(R):
        line_str = ''
        for c in range(C):
            line_str += NUM2REP_DICT[data_array[r, c]]
        print(line_str)



def move_east(sea_cu_map):
    n_row, n_col = sea_cu_map.shape
    cpy_sc_map = np.array(sea_cu_map)
    # move east
    for row in range(n_row):
        for col in range(n_col):
            if sea_cu_map[row, col] == REP2NUM_DICT['>']:
                next_col = col + 1
                if next_col >= n_col:
                    next_col = 0
                if sea_cu_map[row, next_col] == REP2NUM_DICT['.']:
                    cpy_sc_map[row, col] = REP2NUM_DICT['.']
                    cpy_sc_map[row, next_col] = REP2NUM_DICT['>']
    return cpy_sc_map


def move_south(sea_cu_map):
    n_row, n_col = sea_cu_map.shape
    cpy_sc_map = np.array(sea_cu_map)
    # move south
    for row in range(n_row):
        for col in range(n_col):
            if sea_cu_map[row, col] == REP2NUM_DICT['v']:
                next_row = row + 1
                if next_row >= n_row:
                    next_row = 0
                if sea_cu_map[next_row, col] == REP2NUM_DICT['.']:
                    cpy_sc_map[row, col] = REP2NUM_DICT['.']
                    cpy_sc_map[next_row, col] = REP2NUM_DICT['v']
    return cpy_sc_map


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    sc_map = np.array(data)
    
    map_size = sc_map.size

    count = 1

    while True:
        # copy the map to keep track of changes
        old_sc_map = array(sc_map)

        # step
        sc_map = move_east(sc_map)
        sc_map = move_south(sc_map)

        chg = np.equal(old_sc_map, sc_map)

        if np.sum(chg) == map_size:
            break
        count += 1

    return count


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)
    
    # print list - line by line
    # print('\n'.join(str(line) for line in puzzle_data))

    solution1 = part1(puzzle_data, skip=False)
    solution2 = part2(puzzle_data, skip=True)

    return solution1, solution2


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print(f'Please enter at least one file path.')
    else:
        for path in sys.argv[1:]:
            print(f'\n{path}:')
            puzzle_input = pathlib.Path(path).read_text().strip()

            print('Advent of Code 2021 - Day 25')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
