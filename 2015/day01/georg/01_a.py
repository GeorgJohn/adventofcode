

def main() -> None:

    file_name = 'input.txt'

    with open(file_name, 'r') as fp:
        line = fp.read()
        
        floor = 0
        idx = 0

        for f in line:
            if f == '(':
                floor += 1
            elif f == ')':
                floor -= 1

            idx += 1
            if floor == -1:
                break

        print(idx)


def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    main()
