#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def neighbors(x, y, max_x, max_y):
    n = []
    if x - 1 >= 0:
        n.append((x - 1, y))
    if y - 1 >= 0:
        n.append((x, y - 1))
    if x + 1 < max_x:
        n.append((x + 1, y))
    if y + 1 < max_y:
        n.append((x, y + 1))

    return n


def cost_path(came_from, start, goal, field):
    total_cost = 0
    current = goal
    while current != start:
        total_cost += field[current]
        current = came_from[current]
    return total_cost

def dijkstra_search(start, goal, field):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    cost_so_far = {start: 0}
    came_from = {start: None}
    current = start
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in neighbors(current[0], current[1], goal[0]+1, goal[1]+1):
            new_cost = field[next] + cost_so_far[current]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current

    return came_from


with open("input.txt", 'r') as fh:
    input_list = []
    for line in fh:
        input_list.append(list(map(int, line[:-1])))

    field = np.array(input_list, dtype=np.int8)
    goal_point = (field.shape[0] - 1, field.shape[1] -1)
    path = dijkstra_search((0, 0), goal_point, field)
    print(cost_path(path, (0, 0), goal_point, field))
