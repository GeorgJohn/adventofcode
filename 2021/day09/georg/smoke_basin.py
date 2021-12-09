import sys
import copy
import pathlib
import numpy as np


LAPLACIAN_FILTER = np.array([
    [0 , -1, 0],
    [-1 , +4, -1],
    [0 , -1, 0]
    ]) 

# Sobel filter 
SX_FILTER = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
])

SY_FILTER = np.array([
    [-1, -2, -1],
    [+0, +0, +0],
    [+1, +2, +1],
])


def convolution(data_map, applied_filter):
    
    width = data_map.shape[1]
    height = data_map.shape[0]

    # h_border = 10 * np.ones([height, 1], np.int8)
    # v_border = 10 * np.ones([1, width + 2], np.int8)

    # expand_map = np.hstack([h_border, data, h_border])
    # expand_map = np.vstack([v_border, expand_map, v_border])

    # width = expand_map.shape[1]
    # height = expand_map.shape[0]

    w_range = int(np.floor(applied_filter.shape[0]/2))

    filtered_map = np.zeros([height, width], dtype=np.int8)

    # Iterate over each entry of the height map that can be covered by the mask
    for i in range(w_range, width-w_range):
        for j in range(w_range, height-w_range):
            # Then convolute with the mask 
            for k in range(-w_range, w_range+1):
                for h in range(-w_range, w_range+1):
                    filtered_map[j, i] += applied_filter[w_range+h,w_range+k]*data_map[j+h,i+k]

    return filtered_map



def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        line_numbers = [int(digit) for digit in line]
        if len(line_numbers) > 0:
            data.append(line_numbers)
    return np.array(data, dtype=np.int8)


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    # expand borders of the height map
    height, width = data.shape

    border_value = np.max(data)

    h_border = border_value * np.ones([height, 1], np.int8)
    v_border = border_value * np.ones([1, width + 2], np.int8)

    expand_map = np.hstack([h_border, data, h_border])
    expand_map = np.vstack([v_border, expand_map, v_border])

    h, w = expand_map.shape
    minima_map = np.zeros([h, w], dtype=np.int8)

    for i in range(1, h-1):
        for j in range(1, w-1):
            # get horizontal and vertical neighbors
            nb = np.array([expand_map[i-1, j], expand_map[i, j+1], expand_map[i+1, j], expand_map[i, j-1]], dtype=np.int8)
            if expand_map[i, j] < np.min(nb):
                minima_map[i, j] = 1

    minima_map = minima_map[1:h-1, 1:w-1]

    low_points = data[minima_map==1]

    risk_level = low_points + 1

    return np.sum(risk_level)


def move(y, x, command):
    if command == 'up': y -= 1
    elif command == 'down': y += 1
    elif command == 'left': x -= 1
    elif command == 'right': x += 1
    return y, x


def find_edges(y, x, data):
    Y, X = data.shape
    edges = []
    if y - 1 >= 0 and data[y-1, x] != 9:
        edges.append('up')
    if x + 1 < X and data[y, x+1] != 9:
        edges.append('right')
    if y + 1 < Y and data[y+1, x] != 9:
        edges.append('down')
    if x -1 >= 0 and data[y, x-1] != 9:
        edges.append('left')
    
    if len(edges) == 0:
        edges.append(None)

    return edges

def explore(y, x, edges):
    new_nodes = []
    for edge in edges:
        node = move(y, x, edge) 
        new_nodes.append(node)

    return new_nodes


def remove_duplicates(new_nodes, graph):
    
    for entry in graph:
        y, x = entry['node']
        for node in new_nodes:
            if y == node[0] and x == node[1]:
                new_nodes.remove(node)


def isvalid(y, x, data):
    h, w = data.shape
    valid = False
    if 0 <= y < h and 0 <= x < w:
        valid = True
    return valid


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1

    # expand borders of the height map
    height, width = data.shape

    border_value = np.max(data)

    h_border = border_value * np.ones([height, 1], np.int8)
    v_border = border_value * np.ones([1, width + 2], np.int8)

    expand_map = np.hstack([h_border, data, h_border])
    expand_map = np.vstack([v_border, expand_map, v_border])

    h, w = expand_map.shape
    minima_map = np.zeros([h, w], dtype=np.int8)

    for i in range(1, h-1):
        for j in range(1, w-1):
            # get horizontal and vertical neighbors
            nb = np.array([expand_map[i-1, j], expand_map[i, j+1], expand_map[i+1, j], expand_map[i, j-1]], dtype=np.int8)
            if expand_map[i, j] < np.min(nb):
                minima_map[i, j] = 1


    minima_map = minima_map[1:h-1, 1:w-1]

    low_point_idx = np.where(minima_map == 1)

    basin_sizes = []

    for i, j in zip(low_point_idx[0], low_point_idx[1]):

        ly, lx = i, j

        # build graph 
        # nodes -> map locations
        # edges -> move direction

        # graph = [{'node':(ly, lx), 'edges': []}]

        graph = {}

        nodes = [(ly, lx)]

        while nodes:
            
            y, x = nodes.pop(0)

            if (y, x) not in graph.keys():
                graph[(y, x)] = data[y, x]

            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ly = y + dy
                lx = x + dx
                if isvalid(ly, lx, data) and data[ly, lx] > data[y, x] and data[ly, lx] < 9:
                    nodes.append((ly, lx))

        basin_sizes.append(len(graph))

    result = np.product(sorted(basin_sizes)[-3:])

    return result




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

            print('Advent of Code 2021 - Day 09')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
