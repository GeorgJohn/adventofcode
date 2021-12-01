
file_name = '01.txt'


def main() -> None:

    with open(file_name, 'r') as fp:
        
        file = fp.readlines()

        n_inc = 0
        cur_depth = int(file[0])

        for line in file[1:]:

            next_depth = int(line)

            if next_depth > cur_depth:
                # depth increase
                n_inc += 1

            cur_depth = next_depth


        print(n_inc)


if __name__ == '__main__':
    main()
