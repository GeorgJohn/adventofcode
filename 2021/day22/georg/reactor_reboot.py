import sys
import pathlib
import numpy as np


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        
        if len(line) > 0:
            command, xyz_slice = line.split(' ')

            x_str, y_str, z_str = xyz_slice.split(',')

            _, x_str = x_str.split('x=')
            _, y_str = y_str.split('y=')
            _, z_str = z_str.split('z=')

            x_start, x_end = [int(x) for x in x_str.split('..')]
            y_start, y_end = [int(y) for y in y_str.split('..')]
            z_start, z_end = [int(z) for z in z_str.split('..')]

            line = {
                'command': command,
                'x_slice': slice(x_start, x_end+1, 1), 
                'y_slice': slice(y_start, y_end+1, 1), 
                'z_slice': slice(z_start, z_end+1, 1),
                }
            data.append(line)

    return data


def is_in_range(slice_obj, range):
    retval = False
    if slice_obj.start >= -range and slice_obj.stop <= range+1:
        retval = True
    return retval


def add_offset(slice_obj, offset):
    new_slice_obj = slice(slice_obj.start+offset, slice_obj.stop+offset, 1)
    return new_slice_obj


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    cuboid = np.zeros([101, 101, 101], dtype=np.int8)

    for reboot_step in data:

        cmd = reboot_step['command']
        x = reboot_step['x_slice']
        y = reboot_step['y_slice']
        z = reboot_step['z_slice']
        
        if is_in_range(x, 50) and is_in_range(y, 50) and is_in_range(z, 50):
            
            x = add_offset(x, 50)
            y = add_offset(y, 50)
            z = add_offset(z, 50)
            
            if cmd == 'on':
                cuboid[x, y, z] = 1
            else:
                cuboid[x, y, z] = 0


    return np.sum(cuboid)



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

            print('Advent of Code 2021 - Day xx')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
