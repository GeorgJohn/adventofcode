from typing import Callable, List, Tuple


# State indices
DIS = 0  # horizontal distance
DEP = 1  # depth


# Command functions
def forward(state: List[int], cmd: int) -> None:
    state[DIS] += cmd


def up(state: List[int], cmd: int) -> None:
    state[DEP] -= cmd


def down(state: List[int], cmd: int) -> None:
    state[DEP] += cmd


command_dict = {
    'forward': forward,
    'up': up,
    'down': down,
}


def get_obs(line: str) -> Tuple[Callable[[List[int], int], None], int]:

    obs = line.rstrip().split(' ')

    cmd = command_dict[obs[0]]
    value = int(obs[1])

    return (cmd, value)


# Main function
def main(fn: str) -> None:
    
    with open(fn, 'r') as fp:

        state = [0, 0]  # type: List[int]

        for line in fp:
            comand, value = get_obs(line)

            print(type(comand))

            comand(state, value)

        print(f'Current distance: {state[DIS]}; Current depth: {state[DEP]}')
        print(f'AoC Input: {state[DIS] * state[DEP]}')


if __name__ == '__main__':
    
    file_name = '02.txt'
    main(file_name)
