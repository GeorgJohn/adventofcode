import sys
import pathlib


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        # Get only the character with numbers and convert in a list of interger.
        line_numbers = [int(digit) for digit in list(filter(lambda d : d.isdigit() == True, [s for s in line]))]
        if len(line_numbers) > 0:
            data.append(line_numbers)
    return data


def part1(data):
    """ Solve part 1 """
    return 0

def part2(data):
    """ Solve part 2 """
    return 0


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)
    
    # print list line by line
    # print('\n'.join(str(line) for line in puzzle_data))

    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

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
