#!/usr/bin/env python
# -*- coding: utf-8 -*-


P_SUM = 0
P_PROD = 1
P_MIN = 2
P_MAX = 3
P_LITERAL = 4
P_GT = 5
P_LT = 6
P_EQUAL = 7


def prod(multi):
    result = 1
    for m in multi:
        result *= m
    return result


def get_packet(sequence, pos):
    version = int(sequence[pos:pos+3], 2)
    p_type = int(sequence[pos+3:pos+6], 2)
    new_pos = pos + 6
    if p_type == P_LITERAL:
        value = ''
        while sequence[new_pos] != '0':
            value += sequence[new_pos+1:new_pos+5]
            new_pos += 5
        value += sequence[new_pos+1:new_pos+5]
        new_pos += 5
        value = int(value, 2)
    else:
        value = []
        if sequence[new_pos] == '0':
            bit_len = int(sequence[new_pos+1:new_pos+16], 2)
            new_pos += 16
            end_pos = new_pos + bit_len
            while new_pos < end_pos:
                packet, new_pos = get_packet(sequence, new_pos)
                value.append(packet)
        else:
            num_packets = int(sequence[new_pos+1:new_pos+12], 2)
            new_pos += 12
            for i in range(0, num_packets):
                packet, new_pos = get_packet(sequence, new_pos)
                value.append(packet)
    return (version, p_type, value), new_pos


def parse_sequence(sequence):
    packet, position = get_packet(sequence, 0)
    return packet


def check_version(packet):
    version = packet[0]
    if packet[1] != P_LITERAL:
        for p in packet[2]:
            version += check_version(p)

    return version


def execute_op(packet):
    if packet[1] == P_SUM:
        result = sum(list(map(execute_op, packet[2])))
    elif packet[1] == P_PROD:
        result = prod(list(map(execute_op, packet[2])))
    elif packet[1] == P_MIN:
        result = min(list(map(execute_op, packet[2])))
    elif packet[1] == P_MAX:
        result = max(list(map(execute_op, packet[2])))
    elif packet[1] == P_LITERAL:
        result = packet[2]
    elif packet[1] == P_GT:
        a = execute_op(packet[2][0])
        b = execute_op(packet[2][1])
        if a > b:
            result = 1
        else:
            result = 0
    elif packet[1] == P_LT:
        a = execute_op(packet[2][0])
        b = execute_op(packet[2][1])
        if a < b:
            result = 1
        else:
            result = 0
    elif packet[1] == P_EQUAL:
        a = execute_op(packet[2][0])
        b = execute_op(packet[2][1])
        if a == b:
            result = 1
        else:
            result = 0
    else:
        print('op error')
        result = None
    return result

with open("input.txt", 'r') as fh:
    seq = fh.readline()[:-1]
    size = len(seq) * 4
    seq = int(seq, 16)
    seq = '{0:b}'.format(seq)
    seq = ('0' * (size - len(seq))) + seq
    packet = parse_sequence(seq)
    print('result', execute_op(packet))
    print('version', check_version(packet))
