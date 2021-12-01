import numpy as np


file_name = '01.txt'


def main() -> None:

    with open(file_name, 'r') as fp:
        
        file = fp.readlines()
        meas_list = np.array([int(d) for d in file])

        n_inc = 0
        cur_sum = np.sum(meas_list[0:3])

        for n in range(meas_list.shape[0]):
            
            next_sum = np.sum(meas_list[n:n+3])

            if next_sum > cur_sum:
                n_inc += 1

            cur_sum = next_sum

        print(n_inc)



if __name__ == '__main__':
    main()
