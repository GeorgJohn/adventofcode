#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def small_cave_visited_twice(path, is_big):
    small_caves = []
    for n in path:
        if not is_big[n]:
            if not n in small_caves:
                small_caves.append(n)
            else:
                return True
    return False


def explore_paths(paths, node_idx, start_idx, end_idx, adj_mat, is_big):
    update_paths = []
    copy_paths = []
    if not paths:
        copy_paths.append([node_idx])
    else:
        for p in paths:
            new_path = list(p)
            new_path.append(node_idx)
            copy_paths.append(new_path)
    if node_idx != end_idx:
        for i in range(0, adj_mat.shape[0]):
            if i != start_idx:
                if adj_mat[node_idx][i] == 1:
                    if not is_big[i]:
                        for p in copy_paths:
                            if not i in p:
                                update_paths.extend(explore_paths(copy_paths, i, start_idx, end_idx, adj_mat, is_big))
                            elif not small_cave_visited_twice(p, is_big):
                                update_paths.extend(explore_paths(copy_paths, i, start_idx, end_idx, adj_mat, is_big))
                    else:
                        update_paths.extend(explore_paths(copy_paths, i, start_idx, end_idx, adj_mat, is_big))
    else:
        update_paths.extend(copy_paths)

    return update_paths


with open("input.txt", 'r') as fh:
    idx = 0
    node_id = {}
    node_name = {}
    is_big = {}
    edges = []
    for line in fh:
        a = line.split('-')[0]
        b = line.split('-')[1][:-1]
        edges.append((a, b))
        if not a in node_id:
            node_id[a] = idx
            node_name[idx] = a
            if a.isupper():
                is_big[idx] = True
            else:
                is_big[idx] = False
            idx += 1
        if not b in node_id:
            node_id[b] = idx
            node_name[idx] = b
            if b.isupper():
                is_big[idx] = True
            else:
                is_big[idx] = False
            idx += 1

    adjacency_matrix = np.zeros((len(node_id), len(node_id)), dtype=int)
    for edge in edges:
        a = node_id[edge[0]]
        b = node_id[edge[1]]
        adjacency_matrix[a][b] = 1
        adjacency_matrix[b][a] = 1

    valid_paths = explore_paths([], node_id['start'], node_id['start'], node_id['end'], adjacency_matrix, is_big)
    print(len(valid_paths))
