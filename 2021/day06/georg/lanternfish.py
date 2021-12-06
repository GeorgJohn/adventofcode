import sys
import pathlib
import copy


def parse(puzzle_input):
    """ Parse text input in data array. """
    return [int(digit) for digit in puzzle_input.split(',')]


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return 0
    
    fish_state = data

    # BRUTE-FORCE approach. 
    # List will expand with new fish and completely iterated every day
    days = 80
    for _ in range(days):
        for idx in range(len(fish_state)):
            fish_state[idx] -= 1
            if fish_state[idx] < 0:
                # reset timer value
                fish_state[idx] = 6
                # create new fish with timer value 8
                fish_state.append(8)

    # number of lanternfish
    result = len(fish_state)
    return result


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return 0

    initial_state = data

    fish_conter = [0 for i in range(9)]
    fish_conter_cpy = copy.deepcopy(fish_conter)

    # convert state list in a list with number of fish wrt to timer state
    for fish_state in range(len(fish_conter)):
        fish_conter[fish_state] = initial_state.count(fish_state)

    days = 256
    for _ in range(days):
        # Fish where the timer has expired.
        new_fish = fish_conter[0]
        # Reduce timer value
        for idx in range(8):
            fish_conter_cpy[idx] = fish_conter[idx+1]
        # reset internal timer to 6
        fish_conter_cpy[6] += new_fish
        # create new fish with timer value 8
        fish_conter_cpy[8] = new_fish
        fish_conter = copy.deepcopy(fish_conter_cpy)

    # number of lanternfish
    result = sum(fish_conter)
    return result


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

            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
