import sys
import pathlib

PRINT_DATA = False


class SnailfishNumber:

    def __init__(self, x, y=None):
        self.x = x
        self.y = y
        self.level = 0
        self.update_level(level=self.level)

    def update_level(self, level):
        if type(self.x) == SnailfishNumber:
            self.x.update_level(level=self.level+1)
        if type(self.y) == SnailfishNumber:
            self.y.update_level(level=self.level+1)
        
        self.level = level + 1

    def add(self, sfn):
        if self.y is None:
            self.y = sfn
            new_sfn = self
        else:
            new_sfn = SnailfishNumber(self, sfn)
        return new_sfn

    def reduce(self):
        
        if type(self.x) == SnailfishNumber:
            self.x.reduce()
        if type(self.y) == SnailfishNumber:
            self.y.reduce()

        explode = self.explode()

        
    def explode(self):
        if self.level > 4 and type(self.x) == int and type(self.y) == int:
            print(self.x, self.y)
            return True

    def split(self):
        pass

    def __repr__(self) -> str:
        return f'[{self.x}, {self.y}]'



def txt2snailfish(txt_list):

    sf_n = None
    while True:

        if len(txt_list) > 0:
            # this is slow
            next_char = txt_list.pop(0)
        else:
            break
        
        if next_char == '[':
            new_sf_n = txt2snailfish(txt_list=txt_list)
            if sf_n is None:
                sf_n = new_sf_n
            else:
                sf_n = sf_n.add(new_sf_n)

        elif next_char.isdigit():
            if sf_n is None:
                sf_n = SnailfishNumber(int(next_char))
            else:
                sf_n = sf_n.add(int(next_char))
        elif next_char == ']':
            break

    return sf_n


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for input_line in puzzle_input.split('\n'):

        line = []
        if len(input_line) > 0:
            line = [_ for _ in input_line]
            sf = txt2snailfish(line)
            data.append(sf)
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1
    
    final_sf_list = data[0]

    for idx in range(1, len(data)):

        next_sn_list = data[idx]

        final_sf_list.reduce()

        final_sf_list = final_sf_list.add(next_sn_list)

        final_sf_list.reduce()

        print(final_sf_list)



def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)
    
    if PRINT_DATA:
        for line in puzzle_data:
            print(line)

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

            print('Advent of Code 2021 - Day 18')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
