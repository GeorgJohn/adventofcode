from enum import Enum, IntEnum
from typing import Any, List, Tuple


# State indices
DIS = 0  # horizontal distance
DEP = 1  # depth
AIM = 2  # aim


# Command functions
def forward(state: List[int], cmd: int) -> None:
    state[DIS] += cmd
    state[DEP] += state[AIM] * cmd


def up(state: List[int], cmd: int) -> None:
    state[AIM] -= cmd


def down(state: List[int], cmd: int) -> None:
    state[AIM] += cmd


class Commands(Enum):
    FORWARD = forward
    UP = up
    DOWN = down


command_dict = {
    'forward': Commands.FORWARD,
    'up': Commands.UP,
    'down': Commands.DOWN,
}


def get_obs(line: str) -> Tuple[Any, int]:

    obs = line.rstrip().split(' ')

    cmd = command_dict[obs[0]]
    value = int(obs[1])

    return (cmd, value)


# Main function
def main(fn: str) -> None:
    
    with open(fn, 'r') as fp:

        # state: [distance, depth, aim]
        state = [0, 0, 0]  # type: List[int]

        for line in fp:
            comand, value = get_obs(line)

            comand(state, value)

        print(f'Current distance: {state[DIS]}; Current depth: {state[DEP]}; Current aim: {state[AIM]}')
        print(f'AoC Input: {state[DIS] * state[DEP]}')


if __name__ == '__main__':
    file_name = '02.txt'
    main(file_name)
