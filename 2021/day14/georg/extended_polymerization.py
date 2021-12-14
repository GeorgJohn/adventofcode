import sys
import copy
import math
import pathlib


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    rules = {}
    template = []
    for n, line in enumerate(puzzle_input.split('\n')):
        
        if len(line) > 0:
            if n < 1:
                template = line
            else:
                key, value = [s.strip() for s in line.split('->')]
                rules[key] = value
    return [template, rules]


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    polymer_template = copy.deepcopy(data[0])
    rules = data[1]

    n_steps = 10

    for n in range(n_steps):

        new_polymer = ''

        for idx in range(len(polymer_template)-1):

            new_polymer += polymer_template[idx]
            
            key = ''.join(polymer_template[idx:idx + 2])
            if key in rules.keys():
                new_polymer += rules[key]
        
        # add last element
        new_polymer += polymer_template[-1] 


        polymer_template = new_polymer

    all_different_elements = set([elem for elem in polymer_template])

    occurs_dict = {}

    for elem in all_different_elements:
        n = polymer_template.count(elem)
        occurs_dict[elem] = n
    

    min = math.inf
    max = 0

    for elem, occurs in occurs_dict.items():

        if occurs < min:
            min_elem = elem
            min = occurs
        if occurs > max:
            max_elem = elem
            max = occurs

    result = occurs_dict[max_elem] - occurs_dict[min_elem]

    return result



def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1

    polymer_template = copy.deepcopy(data[0])
    rules = data[1]

    counter_elements = {}
    rule_tracker_template = {}

    for key, rule in rules.items():
        counter_elements[rule] = 0
        rule_tracker_template[key] = 0

    n_steps = 40

    for idx in range(len(polymer_template) - 1):

        poly = ''.join(polymer_template[idx:idx+2])

        for elem in poly:
            counter_elements[elem] += 1

        rule_tracker = copy.deepcopy(rule_tracker_template)

        rule_tracker[poly] += 1

        for n in range(n_steps):
            
            new_rule_tracker = copy.deepcopy(rule_tracker_template)

            for rule, occur in rule_tracker.items():
                new_elem = rules[rule]
                counter_elements[new_elem] += occur

                new_rule_tracker[rule[0] + new_elem] += occur
                new_rule_tracker[new_elem + rule[1]] += occur

            rule_tracker = copy.deepcopy(new_rule_tracker)

    # delete double counted elements
    for idx in range(len(polymer_template) - 2):
        elem = polymer_template[idx + 1]
        counter_elements[elem] -= 1

    min = math.inf
    max = 0

    for elem, occurs in counter_elements.items():

        if occurs < min:
            min_elem = elem
            min = occurs
        if occurs > max:
            max_elem = elem
            max = occurs

    result = counter_elements[max_elem] - counter_elements[min_elem]

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

            print('Advent of Code 2021 - Day 14')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
