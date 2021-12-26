#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

re_range = re.compile(r'target area: x=([0-9]+)\.\.([0-9]+), y=(\-[0-9]+)\.\.(\-[0-9]+).*')

with open("input.txt", 'r') as fh:
    input = fh.readline()
    m = re_range.match(input)
    x_range = int(m.group(1)), int(m.group(2))
    y_range = int(m.group(3)), int(m.group(4))
    print(sum(range(0, -y_range[0])))


