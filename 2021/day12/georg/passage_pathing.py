import sys
import copy
import pathlib

from typing import Dict, List


class Graph1:

    def __init__ (self):
        self.allpaths = []

    def FindAllPaths(self, adjlist : Dict[int, List[int]] , src : int, dst : int) -> int:
        # Clear previously stored paths
        path = []
        path.append(src)
        print("Source : " + str(src) + " Destination : " +  str(dst))

        # Use depth first search (with backtracking) to find all the paths in the graph
        self.DFS(adjlist, src, dst, path)

        # Print all paths
        # self.Print()

        return len(self.allpaths)


    def Print (self):
        # print (self.allpaths)
        for path in self.allpaths:
            print("Path : " + str(path))
        # self.allpaths.clear()

    # This function uses DFS at its core to find all the paths in a graph
    def DFS(self, adjlist : Dict[int, List[int]], src : int, dst : int, path : List[int]):
        if(src == dst):
            self.allpaths.append(copy.deepcopy(path))
        else:
            for adjnode in adjlist[src]:
                if adjnode.isupper() or adjnode not in path:
                    path.append(adjnode)
                    self.DFS(adjlist, adjnode, dst, path)
                    path.pop()


class Graph2:

    def __init__ (self):
        self.allpaths = []

    def FindAllPaths(self, adjlist : Dict[int, List[int]] , src : int, dst : int) -> int:
        # Clear previously stored paths
        path = []
        path.append(src)
        print("Source : " + str(src) + " Destination : " +  str(dst))

        # Use depth first search (with backtracking) to find all the paths in the graph
        self.DFS(adjlist, src, dst, path)

        result_path = []

        for path in self.allpaths:

            first_double = False
            delete_path = False
            node_list = []
            for node in path:
                if node not in ['start', 'end']:
                    if node.islower() and path.count(node) >= 2:
                        if first_double and node not in node_list:
                           delete_path = True 
                        elif not first_double:
                            first_double = True
                            node_list.append(node)

            if not delete_path:
                result_path.append(path)

        self.allpaths = result_path

        # Print all paths
        # self.Print()

        return len(result_path)


    def Print (self):
        # print (self.allpaths)
        for path in self.allpaths:
            print("Path : " + str(path))
        # self.allpaths.clear()

    # This function uses DFS at its core to find all the paths in a graph
    def DFS(self, adjlist : Dict[int, List[int]], src : int, dst : int, path : List[int]):
        if(src == dst):
            self.allpaths.append(copy.deepcopy(path))
        else:
            for adjnode in adjlist[src]:
                if adjnode.islower() and path.count(adjnode) >= 2:
                        pass
                else:
                    path.append(adjnode)
                    self.DFS(adjlist, adjnode, dst, path)
                    path.pop()


def parse(puzzle_input):
    """ Parse text input in data array. """
    
    data = []
    for line in puzzle_input.split('\n'):
        # Get only the character with numbers and convert in a list of interger.
        if len(line) > 0:
            start, end = line.split('-')
            if end == 'start' or start == 'end':
                data.append([end, start])
            else:
                data.append([start, end])
    return data


def part1(data, skip):
    """ Solve part 1 """
    if skip:
        return -1

    cave_map = copy.deepcopy(data)

    nodes = {}

    for connection in cave_map:
        for node in connection:
            if node not in nodes.keys():
                nodes[node] = []
    
    for node, neighbors in nodes.items():
        for connection in cave_map:
            if node in connection:
                idx = connection.index(node)
                neighbor = connection[1-idx]
                if neighbor != 'start' and node != 'end':
                    neighbors.append(neighbor)

    graph = Graph1()

    n_paths = graph.FindAllPaths(nodes, 'start', 'end')

    return n_paths


def part2(data, skip):
    """ Solve part 2 """
    if skip:
       return -1

    cave_map = copy.deepcopy(data)

    nodes = {}

    for connection in cave_map:
        for node in connection:
            if node not in nodes.keys():
                nodes[node] = []
    
    for node, neighbors in nodes.items():
        for connection in cave_map:
            if node in connection:
                idx = connection.index(node)
                neighbor = connection[1-idx]
                if neighbor != 'start' and node != 'end':
                    neighbors.append(neighbor)

    graph = Graph2()

    n_paths = graph.FindAllPaths(nodes, 'start', 'end')

    return n_paths


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

            print('Advent of Code 2021 - Day 12')
            solutions = solve(puzzle_input)
            for n, s in enumerate(solutions):
                print(f'The puzzle solution of part {n+1} is: {s}')
