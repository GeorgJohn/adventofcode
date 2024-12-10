import sys
import pathlib


P_SUM = 0
P_PROD = 1
P_MIN = 2
P_MAX = 3
P_LITERAL = 4
P_GT = 5
P_LT = 6
P_EQUAL = 7

LITERAL_GRP_SIZE = 5


def prod(multi):
    result = 1
    for m in multi:
        result *= m
    return result


def parse(puzzle_input):
    """ Parse text input in and decode from hex to binary """
    # The file can only contain one line. 
    # If not only the last line will be decode
    data = None
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            size = len(line) * 4
            seq = int(line, 16)
            seq = '{0:b}'.format(seq)
            seq = ('0' * (size - len(seq))) + seq
            data = seq
    return data


def decode_pkg(pkg, pkg_pos):
    # decode header
    new_pkg_pos = pkg_pos + 3
    version = int(pkg[pkg_pos:new_pkg_pos], 2)
    start_idx = new_pkg_pos
    new_pkg_pos += 3
    pkg_id = int(pkg[start_idx:new_pkg_pos], 2)

    if pkg_id == P_LITERAL:
        ########################
        # literal value packet #
        ########################
        literal_value = ''
        while pkg[new_pkg_pos] != '0':
            literal_value += pkg[new_pkg_pos+1:new_pkg_pos+LITERAL_GRP_SIZE]
            new_pkg_pos += LITERAL_GRP_SIZE
        # handle last group
        literal_value += pkg[new_pkg_pos+1:new_pkg_pos+LITERAL_GRP_SIZE]
        new_pkg_pos += LITERAL_GRP_SIZE
        literal_value = int(literal_value, 2)
        sub_pkgs = literal_value
    else:
        ###################
        # operator packet #
        ###################
        sub_pkgs = []
        length_type_id = pkg[new_pkg_pos]
        new_pkg_pos += 1

        if length_type_id == '1':
            bit_num_len = 11
            start_idx = new_pkg_pos
            new_pkg_pos += bit_num_len
            n_sub_pkg = int(pkg[start_idx:new_pkg_pos], 2)
            for _ in range(n_sub_pkg):
                sub_pkg, new_pkg_pos = decode_pkg(pkg, new_pkg_pos)
                sub_pkgs.append(sub_pkg)
        elif length_type_id == '0':
            bit_num_len = 15
            start_idx = new_pkg_pos
            new_pkg_pos += bit_num_len
            bit_len = int(pkg[start_idx:new_pkg_pos], 2)
            end_pkg_pos = new_pkg_pos + bit_len
            while new_pkg_pos < end_pkg_pos:
                sub_pkg, new_pkg_pos = decode_pkg(pkg, new_pkg_pos)
                sub_pkgs.append(sub_pkg)
        else:
            sys.exit('Error in packet string.')

    return (version, pkg_id, sub_pkgs), new_pkg_pos


def sum_up_version(packet):
    version = packet[0]
    if packet[1] != P_LITERAL:
        for p in packet[2]:
            version += sum_up_version(p)

    return version


def evaluate(packet):
    if packet[1] == P_SUM:
        result = sum(list(map(evaluate, packet[2])))
    elif packet[1] == P_PROD:
        result = prod(list(map(evaluate, packet[2])))
    elif packet[1] == P_MIN:
        result = min(list(map(evaluate, packet[2])))
    elif packet[1] == P_MAX:
        result = max(list(map(evaluate, packet[2])))
    elif packet[1] == P_LITERAL:
        result = packet[2]
    elif packet[1] == P_GT:
        a = evaluate(packet[2][0])
        b = evaluate(packet[2][1])
        if a > b:
            result = 1
        else:
            result = 0
    elif packet[1] == P_LT:
        a = evaluate(packet[2][0])
        b = evaluate(packet[2][1])
        if a < b:
            result = 1
        else:
            result = 0
    elif packet[1] == P_EQUAL:
        a = evaluate(packet[2][0])
        b = evaluate(packet[2][1])
        if a == b:
            result = 1
        else:
            result = 0
    else:
        print('op error')
        result = None
    return result


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1
    pkgs, _ = decode_pkg(data, 0)
    version_num = sum_up_version(pkgs)
    return version_num


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1
    pkgs, _ = decode_pkg(data, 0)
    value = evaluate(pkgs)
    return value


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)
     
    solution1 = part1(str(puzzle_data), skip=False)
    solution2 = part2(str(puzzle_data), skip=False)

    return solution1, solution2


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print(f'Please enter at least one file path.')
    else:
        for path in sys.argv[1:]:
            print(f'\n{path}:')
            puzzle_input = pathlib.Path(path).read_text().strip()

            print('Advent of Code 2021 - Day 16')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
