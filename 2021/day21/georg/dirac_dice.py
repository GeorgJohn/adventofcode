import sys
import pathlib


class Player():

    def __init__(self, id, start_pos) -> None:
        self.id = id
        self.pos = start_pos
        self.score = 0

    def move(self, steps):
        
        done = False
        new_pos = self.pos + steps
        new_pos = new_pos % 10
        if new_pos == 0:
            self.pos = 10
        else:
            self.pos = new_pos

        self.score += self.pos    
        if self.score >= 1000:
            done = True
    
        return done



def parse(puzzle_input):
    """ Parse text input in data array. """
    data = {}
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            input = [int(sub_line) for sub_line in line.split(' ') if sub_line.isdigit()]
            data[input[0]] = input[1]
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    players = []

    deter_dice = 0

    for ply_id in data:
        players.append(Player(ply_id, data[ply_id]))

    N = len(players)
    player_idx = 0
    result = 0
    while True:

        current_player = players[player_idx]

        player_idx += 1
        if player_idx >= N:
            player_idx = 0

        rolls_sum = 0
        for i in range(3):
            deter_dice += 1
            rolls_sum += deter_dice

        done = current_player.move(rolls_sum)

        if done:
            loser_score = 0
            for player in players:
                if player.score < 1000:
                    loser_score = player.score
            result = loser_score * deter_dice
            break

    return result


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1


def solve(puzzle_input):
    """ Solve puzzle """
    puzzle_data = parse(puzzle_input)

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

            print('Advent of Code 2021 - Day 21')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
