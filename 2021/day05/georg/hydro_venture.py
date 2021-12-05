import sys
import pathlib

import numpy as np

def line2coordinates(line):
    xy1, _, xy2  = line.split()
    xy1 = [int(n) for n in xy1.split(',')]
    xy2 = [int(n) for n in xy2.split(',')]
    return np.array([xy1, xy2])

def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = np.array([])
    for line in puzzle_input.split('\n'):
        coord = line2coordinates(line=line)
        if data.size > 0:
            data = np.vstack([data, np.expand_dims(coord, axis=0)])
        else:
            data = np.expand_dims(coord, axis=0)

    return data


def search_horizontal_lines(points):
    return points[points[:, 0, 1] == points[:, 1, 1]]

def search_vertical_lines(points):
    return points[points[:, 0, 0] == points[:, 1, 0]]

def search_diag_lines(points):
    points = points[points[:, 0, 1] != points[:, 1, 1]]
    return points[points[:, 0, 0] != points[:, 1, 0]] 


def part1(data):
    
    hp = search_horizontal_lines(data)
    vp = search_vertical_lines(data)

    occupancy_map = np.zeros([hp[:, :, 1].max()+1, vp[:, :, 0].max()+1], dtype=np.int8)

    # mark the horizontal lines on the map
    for coord in hp:
        xy1, xy2 = coord
        # sort indices
        xx = sorted([xy1[0], xy2[0]])
        occupancy_map[xy1[1], xx[0]:xx[1]+1] += 1

    # mark the vertical lines on the map
    for coord in vp:
        xy1, xy2 = coord
        # sort indices
        yy = sorted([xy1[1], xy2[1]])
        occupancy_map[yy[0]:yy[1]+1, xy1[0]] += 1

    return occupancy_map[occupancy_map >= 2].size


def part2(data):

    # create occupancy map
    occupancy_map = np.zeros([data[:, :, 1].max()+1, data[:, :, 0].max()+1], dtype=np.int8)

    h_lines = search_horizontal_lines(data)
    v_lines = search_vertical_lines(data)
    d_lines = search_diag_lines(data)

    # mark the horizontal lines on the map
    for coord in h_lines:
        xy1, xy2 = coord
        # sort indices
        xx = sorted([xy1[0], xy2[0]])
        occupancy_map[xy1[1], xx[0]:xx[1]+1] += 1

    # mark the vertical lines on the map
    for coord in v_lines:
        xy1, xy2 = coord
        # sort indices
        yy = sorted([xy1[1], xy2[1]])
        occupancy_map[yy[0]:yy[1]+1, xy1[0]] += 1

    # mark the diagonal lines on the map
    for coord in d_lines:
        xy1, xy2 = coord

        xx = [xy1[0], xy2[0]]
        yy = [xy1[1], xy2[1]]

        # correction of indices 
        xx[1] = xx[1] - 1 if xx[0] > xx[1] else xx[1] + 1
        yy[1] = yy[1] - 1 if yy[0] > yy[1] else yy[1] + 1
        
        # find the slice direction
        y_step = -1 if yy[0] > yy[1] else 1
        x_step = -1 if xx[0] > xx[1] else 1

        # interate diagonal
        for x, y in zip(range(xx[0], xx[1], x_step), range(yy[0], yy[1], y_step)):
            occupancy_map[y, x] += 1

    result = occupancy_map[occupancy_map >= 2].size
    return result



def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_input = parse(puzzle_input)
    
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)

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
