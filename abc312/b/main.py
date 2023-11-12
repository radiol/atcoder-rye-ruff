from __future__ import annotations

import sys
from itertools import product

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())

    grid = [list(input().strip()) for _ in range(N)]

    for i in range(N - 8):
        for j in range(M - 8):
            if check([row[j : j + 9] for row in grid[i : i + 9]]):
                print(i + 1, j + 1)


def check(grid: list[list[str]]):  # noqa: C901, PLR0911
    for x, y in product(range(3), repeat=2):
        if grid[x][y] != "#":
            return False
    for x, y in product(range(6, 9), repeat=2):
        if grid[x][y] != "#":
            return False
    for x in range(4):
        if grid[x][3] != ".":
            return False
        if grid[3][x] != ".":
            return False
    for x in range(5, 9):
        if grid[x][5] != ".":
            return False
        if grid[5][x] != ".":
            return False

    return True


if __name__ == "__main__":
    main()
