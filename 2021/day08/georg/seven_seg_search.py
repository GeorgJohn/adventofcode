""" seven segment search """
import sys
import pathlib


SEVEN_SEGMENT = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        signal_patterns, output_values = [sub_str.strip().split(' ') for sub_str in line.split('|')]
        data.append([signal_patterns, output_values])
    return data


def recover_segments(digits):

    segment_map = dict()

    seg2 = []  # corresponds to 1
    seg3 = []  # corresponds to 7
    seg4 = []  # corresponds to 4
    seg5 = []  # corresponds to 2,3,5
    seg6 = []  # corresponds to 0,6,9
    seg7 = []  # corresponds to 8

    for digit in digits:
        if len(digit) == 2: seg2.append(sorted(digit))
        elif len(digit) == 3: seg3.append(sorted(digit))
        elif len(digit) == 4: seg4.append(sorted(digit))
        elif len(digit) == 5: seg5.append(sorted(digit))
        elif len(digit) == 6: seg6.append(sorted(digit))
        elif len(digit) == 7: seg7.append(sorted(digit))

    assert len(seg2) == 1
    assert len(seg3) == 1
    assert len(seg4) == 1
    assert len(seg5) == 3
    assert len(seg6) == 3
    assert len(seg7) == 1
    
    one = seg2[0]
    seven = seg3[0]
    four = seg4[0]
    eight = seg7[0]

    # decode segment a
    for seg in seven:
        if seg not in one:
            segment_map['a'] = seg 

    # find segment b, d
    bd = []
    for seg in four:
        if seg not in one:
            bd.append(seg)

    # find a, d, g
    adg = []
    for i in range(5):
        seg = seg5[0][i]
        if seg in seg5[1] and seg in seg5[2]:
            adg.append(seg)

    # find d, g
    dg = []
    for seg in adg:
        if seg != segment_map['a']:
            dg.append(seg)

    # decode b, d 
    for seg in bd:
        if seg in dg:
            segment_map['d'] = seg
        else:
            segment_map['b'] = seg

    # decode g
    for seg in dg:
        if seg != segment_map['d']:
            segment_map['g'] = seg

    # decode e
    for seg in eight:
        if not(seg in one or seg in segment_map.values()):
            segment_map['e'] = seg

    # find five
    for digit in seg5:
        if segment_map['b'] in digit:
            fife = digit

    # decode f 
    for seg in fife:
        if not seg in segment_map.values():
            segment_map['f'] = seg
            break
    
    # decode c
    for seg in eight:
        if not seg in segment_map.values():
            segment_map['c'] = seg
            break

    return segment_map


def decode_digit(digit_str, segment_map):
    # invert map
    decode_dict = {v:k for k,v in segment_map.items()}

    decode_string = ''
    for seg in digit_str:
        decode_string += decode_dict[seg]

    # sort
    decode_string = ''.join(sorted(decode_string))

    return SEVEN_SEGMENT[decode_string]



def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return 0
    
    n_out_digit = 0

    for entry in data:
        for digit in entry[1]:
            if len(digit) <= 4 or len(digit) == 7:
                n_out_digit += 1

    return n_out_digit



def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return 0

    sum = 0
    for entry in data:
        seg_map = recover_segments(entry[0])

        digits = ''
        for digit_str in entry[1]:
            digit = decode_digit(digit_str, seg_map)
            digits += digit
        sum += int(digits)

    return sum


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

            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
