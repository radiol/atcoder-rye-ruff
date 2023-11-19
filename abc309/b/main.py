from __future__ import annotations

import sys
from copy import deepcopy

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())

    grid = [list(input().strip()) for _ in range(N)]

    ans = deepcopy(grid)
    ans[0] = deepcopy(grid[1][0:1] + grid[0][:-1])
    ans[-1] = deepcopy(grid[-1][1:] + grid[-2][-1:])
    for i in range(1, N - 1):
        ans[i][0] = grid[i + 1][0]
        ans[i][-1] = grid[i - 1][-1]
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
