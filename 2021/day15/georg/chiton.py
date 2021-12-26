import sys
import pathlib

import numpy as np

# use big interger to avoid float values
MAX_VALUE = 99999


def parse(puzzle_input):
    """ Parse text input in data array. """
    data = []
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            line_numbers = [int(digit) for digit in line]
            data.append(line_numbers)
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1
    """ 
    The value function is defined as the sum of cost you get 
    when you start at state s and act optimally afterwards.
    So, solving the value function for all states leads to the result. 
    """
    # constants
    height, width = data.shape

    # Initialize the value function table with large values to avoid wrong minimas.
    risk_value_map = np.ones_like(data, dtype=np.int32) * MAX_VALUE
    while True:
        # Add up all values to track progress.
        sum_value = np.sum(risk_value_map)

        for r in range(height-1, -1, -1):
            for c in range(width-1, -1, -1):
                if r == height-1 and c == width-1:
                    risk_value_map[r, c] = 0
                else:
                    # Find the optimal value in the neighborhood.
                    v_min = MAX_VALUE
                    for action in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        idr = r + action[0]
                        idc = c + action[1]

                        if 0 <= idr < height and 0 <= idc < width:
                            if risk_value_map[idr, idc] + data[idr, idc] <= v_min:
                                # Update rule: V(x) = C(x) + V_min(X)
                                v_min = risk_value_map[idr, idc] + data[idr, idc]

                    risk_value_map[r, c] = v_min

        # Check if the value function converges. 
        cv = sum_value - np.sum(risk_value_map)
        if cv < 1:
            break
    
    # The value in the top left corner is the result.
    return risk_value_map[0, 0]


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1


    # Create start map for the 5 new rows of maps.
    height, width = data.shape
    map_parts = np.zeros([5, height, width], dtype=np.int32)
    map_parts[0] = data[:]
    for i in range(1, 5):
        map_parts[i] = map_parts[i-1] + 1
        map_parts[map_parts > 9] = 1

    # Create full map by expand row by row.
    full_map = None
    for row in range(5):
        # Initialize with first column part
        map_row = np.array(map_parts[row]) 
        
        for col in range(1, 5):
            new_map_part = np.array(map_row[:, (col-1)*width:col*width]) + 1
            new_map_part[new_map_part>9] = 1
            map_row = np.hstack([map_row, new_map_part])
        
        if full_map is None:
            full_map = np.array(map_row)
        else:
            full_map = np.vstack([full_map, map_row])

    # Solve value function for the expand map
    return part1(full_map, skip=False)


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)

    solution1 = part1(np.array(puzzle_data, dtype=np.int32), skip=False)
    solution2 = part2(np.array(puzzle_data, dtype=np.int32), skip=False)

    return solution1, solution2


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print(f'Please enter at least one file path.')
    else:
        for path in sys.argv[1:]:
            print(f'\n{path}:')
            puzzle_input = pathlib.Path(path).read_text().strip()

            print('Advent of Code 2021 - Day 15')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
