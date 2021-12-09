#!/usr/bin/env python3
from typing import Dict, Tuple
import numpy as np


class Grid:
    def __init__(self) -> None:
        # Create some values in a grid.
        self.cells = np.array([[0 if x in (0, 19) or y in (0, 9) else (7 * x + 3 * y) % 20
            for x in range (20)] for y in range(10)])
        print(self.cells)

    def search_upward(self, x: int, y: int) -> None:
        # Search 4 neighbor cells for increasing values and collect all cells starting from (x, y).
        results = {}  # type: Dict[Tuple[int, int], int]
        checks = [(x, y)]
        while checks:
            x, y = checks.pop(0)
            if (x, y) not in results.keys():
                print(f"collect {(x, y)}")
                results[(x, y)] = self.cells[y][x]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if self.cells[y + dy][x + dx] > self.cells[y][x]:
                    print(f"check {(x + dx, y + dy)}")
                    checks.append((x + dx, y + dy))
        print(results)


if __name__ == '__main__':
    Grid().search_upward(4, 4)

