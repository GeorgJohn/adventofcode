import copy
import numpy as np



# Main function
def main(fn):
    
    with open(fn, 'r') as fp:

        # get bingo master keys
        master_keys = fp.readline().strip()
        master_keys = np.array([int(number) for number in master_keys.split(',')])

        # read boards to a list structure
        tmp_board = []
        board_collection = []

        for line in fp:
            line = line.strip()
            if line:
                new_board = False
                tmp_board.append([int(number) for number in line.split()])
            else:
                new_board = True
                if tmp_board:
                    board_collection.append(copy.deepcopy(tmp_board))
            if new_board:
                tmp_board = []

        # convert list structure to a numpy array
        boards = np.array(board_collection)

        # create a occupancy map with the same size
        board_map = np.zeros_like(boards)
        b, r, c = boards.shape

        # create a winner map to determine the last winner board
        winner_map = np.zeros([b])
        found_last_winner = False

        # start bingo game
        for key in master_keys:
            # map the occupancies        
            board_map[boards==key] = 1

            # find rows and columns which are fully occupied
            for n_board, sub_map in enumerate(board_map):
                sum_row = np.sum(sub_map, axis=1)
                sum_col = np.sum(sub_map, axis=0)

                if r in sum_row or c in sum_col:
                    winner_map[n_board] = 1

                # check if all maps already win
                if np.sum(winner_map) == b:
                    found_last_winner = True
                    break

            if found_last_winner:
                break

    
        # get unmarked values of the winner board
        unmarked_values = boards[n_board, board_map[n_board] == 0]

        result = np.sum(unmarked_values) * key
        print(f'Puzzle result: {result}')


if __name__ == '__main__':
    
    file_name = '04.txt'
    main(file_name)
