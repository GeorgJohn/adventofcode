#!/usr/bin/env python
# -*- coding: utf-8 -*-

T_PACKET_VERSION = 0
T_PACKET_TYPE = 1
T_PACKET_LITERAL = 2
T_PACKET_LEN = 3



TOKEN_VERSION = 0
TOKEN_TYPE = 1
TOKEN_NUMBER = 2
TOKEN_LEN_11 = 3
TOKEN_LEN_15 = 4


def get_token(sequence, pos, state):
    if state == T_PACKET_VERSION:
        t_type = TOKEN_VERSION
        content = sequence[pos: pos + 3]
        new_state = T_PACKET_TYPE
        new_pos = pos + 3
    elif state == T_PACKET_TYPE:
        t_type = TOKEN_TYPE
        content = sequence[pos: pos + 3]
        new_pos = pos + 3
        if int(sequence[pos: pos + 3], 2) == 4:
            new_state = T_PACKET_LITERAL
        else:
            new_state = T_PACKET_LEN
    elif state == T_PACKET_LITERAL:
        t_type = TOKEN_NUMBER
        content = sequence[pos + 1: pos + 5]
        new_pos = pos + 5
        if sequence[pos] == '1':
            new_state = state
        else:
            new_state = T_PACKET_VERSION
    elif state == T_PACKET_LEN:
        if sequence[pos] == '1':
            t_type = TOKEN_LEN_11
            content = sequence[pos + 1: pos + 12]
            new_pos = pos + 12
        else:
            t_type = TOKEN_LEN_15
            content = sequence[pos + 1: pos + 16]
            new_pos = pos + 16
        new_state = T_PACKET_VERSION
    else:
        print('error')
        return None

    return (t_type, content), new_state, new_pos


def parse_sequence(sequence):
    token_list = []
    position = 0
    end = len(sequence)
    current_state = T_PACKET_VERSION
    while position != end:
        token, current_state, position = get_token(sequence, position, current_state)
        token_list.append(token)
    version_sum  = 0
    for token in token_list:
        if token[0] == TOKEN_VERSION:
            version_sum += int(token[1], 2)
    print(version_sum)


with open("input.txt", 'r') as fh:
    seq = fh.readline()[:-1]
    seq = int(seq, 16)
    seq = '{0:b}'.format(seq)
    parse_sequence(seq[:-5])


