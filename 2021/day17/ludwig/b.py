#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

re_range = re.compile(r'target area: x=([0-9]+)\.\.([0-9]+), y=(\-[0-9]+)\.\.(\-[0-9]+).*')


def simulate_shoot(v_x, v_y, target_area):
    pos_x = 0
    pos_y = 0
    v_x_new = v_x
    v_y_new = v_y
    while pos_x <= target_area[0][1] and target_area[1][0] <= pos_y:
        if target_area[0][0] <= pos_x <= target_area[0][1] and target_area[1][0] <= pos_y <= target_area[1][1]:
            return True
        pos_x += v_x_new
        pos_y += v_y_new
        if v_x_new > 0:
            v_x_new -= 1
        v_y_new -= 1

    return False


with open("input.txt", 'r') as fh:
    input = fh.readline()
    m = re_range.match(input)
    x_range = int(m.group(1)), int(m.group(2))
    y_range = int(m.group(3)), int(m.group(4))
    y_max = -y_range[0] - 1
    y_min = y_range[0]
    x_min = 0
    for i in range(0, x_range[0]):
        dist = sum(range(0, i+1))
        if dist >= x_range[0]:
            x_min = i
            break
    x_max = x_range[1]
    hit_list = []
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if simulate_shoot(x, y, (x_range, y_range)):
                hit_list.append((x, y))

    print(len(hit_list))
