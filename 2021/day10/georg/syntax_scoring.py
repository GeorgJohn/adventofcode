from ctypes import LittleEndianStructure
import sys
import pathlib


SCORE_CORRUPTED = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
SCORE_INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
OPEN_BRACKETS = ['(', '[', '{', '<']
CLOSE_BRACKETS = [')', ']', '}', '>']


class NavigationSubsystemLine:

    def __init__(self, line):
        self.chunks = []
        self.memory = []
        for bracket in line:
            if bracket in OPEN_BRACKETS:
                self.memory.append(bracket)
            else:
                self.chunks.append([self.memory.pop(), bracket])

    def is_corrupted(self):
        """ 
        Check if chunks are corrupted. 
        This means that the open bracket does not match the closed bracket. 
        """
        corrupted = False
        for chunk in self.chunks:
            open_idx = OPEN_BRACKETS.index(chunk[0])
            close_idx = CLOSE_BRACKETS.index(chunk[1])
            if open_idx != close_idx:
                corrupted = True
        return corrupted

    def is_complete(self):
        """ Name wrapper function. """
        return self.is_corrupted()

    def first_illegal_character(self):
        """
        Find the first mismatch in chunks
        """
        illegal_character = ''
        for chunk in self.chunks:
            open_idx = OPEN_BRACKETS.index(chunk[0])
            close_idx = CLOSE_BRACKETS.index(chunk[1])
            # found first illegal character
            if open_idx != close_idx:
                illegal_character = chunk[1]
                break
        return illegal_character

    def complete_line(self):
        """ Find closing brackets for all remaining open brackets. """
        completion = []
        for open_bracket in reversed(self.memory):
            open_idx = OPEN_BRACKETS.index(open_bracket)
            close_bracket = CLOSE_BRACKETS[open_idx]
            completion.append(close_bracket)
        return completion


def parse(puzzle_input):
    """ Parse text input in data array. """
    data = []
    for line in puzzle_input.split('\n'):
        # Get only the character with numbers and convert in a list of interger.
        chunk_line = [char for char in line.strip()]
        if len(chunk_line) > 0:
            data.append(chunk_line)
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    # Find illegal characters
    illegal_character = []
    for line in data:
        nsl = NavigationSubsystemLine(line)
        if nsl.is_corrupted():
            illegal_character.append(nsl.first_illegal_character())

    # Calculate score
    score = 0
    for char in illegal_character:
        score += SCORE_CORRUPTED[char]
    return score


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1

    scores = []
    for line in data:
        nsl = NavigationSubsystemLine(line)
        if not nsl.is_complete():
            score = 0
            completion = nsl.complete_line()
            # Calculate score for completion.
            for close_bracket in completion:
                score *= 5
                score_value = SCORE_INCOMPLETE[close_bracket]
                score += score_value
            scores.append(score)

    # Find median
    # There will always be an odd number of scores to consider.
    scores = sorted(scores)
    n_scores = len(scores)
    middle_score = scores[n_scores//2]
    return middle_score


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

            print('Advent of Code 2021 - Day 10')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
