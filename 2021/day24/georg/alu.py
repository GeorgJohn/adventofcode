import sys
import pathlib


class ModelNumberGenerator:

    def __init__(self) -> None:
        pass

    def __iter__(self):
        for w14 in range(9, 0, -1):
            for w13 in range(9, 0, -1):
                for w12 in range(9, 0, -1):
                    for w11 in range(9, 0, -1):
                        for w10 in range(9, 0, -1):
                            for w9 in range(9, 0, -1):
                                for w8 in range(9, 0, -1):
                                    for w7 in range(9, 0, -1):
                                        for w6 in range(9, 0, -1):
                                            for w5 in range(9, 0, -1):
                                                for w4 in range(9, 0, -1):
                                                    for w3 in range(9, 0, -1):
                                                        for w2 in range(9, 0, -1):
                                                            for w1 in range(9, 0, -1):
                                                                yield [w14, w13, w12, w11, w10, w9, w8, w7, w6, w5, w4, w3, w2, w1]


class ALU:

    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    def div(a, b):
        if b == 0:
            return None
        else:
            return a // b

    def mod(a, b):
        if a < 0 or b <= 0:
            return None
        else:
            return a % b

    def eql(a, b):
        return int(a == b)


def parse(puzzle_input):
    """ Parse text input to instruction list. """
    alu_dict = ALU.__dict__
    data = []
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            line = line.split(' ')
            if len(line) < 3:
                data.append((line[0], line[1]))
            else:
                data.append((alu_dict[line[0]], line[1], line[2]))
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1
    
    mn_gen = ModelNumberGenerator()
    instructions = data

    count = 1

    for model_number in mn_gen:
        
        mn_idx = 0
        variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

        for ins in instructions:            
            if ins[0] == 'inp':
                variables['w'] = model_number[mn_idx]
                mn_idx += 1
            else:
                a = variables[ins[1]]
                if ins[2] not in variables:
                    b = int(ins[2])
                else:
                    b = variables[ins[2]]
                
                a = ins[0](a, b)
                if a is not None:
                    variables[ins[1]] = a
                else:
                    pass

        if variables['z'] == 0:
            break
        else:
            count += 1
            if count % 1000000 == 0:
                z = variables['z']
                print(f'No solution found after {count} steps! z: {z}')

    return int("".join(list(map(str, model_number))))



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

            print('Advent of Code 2021 - Day 24')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
