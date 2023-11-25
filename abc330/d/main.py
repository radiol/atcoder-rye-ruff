from __future__ import annotations

import sys

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

    cnt_column = [0] * N
    for i in range(N):
        for j in range(N):
            if grid[j][i] == "o":
                cnt_column[i] += 1

    ans = 0
    for row in grid:
        cnt = row.count("o")
        if cnt < 2:
            continue
        for j, c in enumerate(row):
            if c != "o":
                continue
            ans += (cnt_column[j] - 1) * (cnt - 1)
    print(ans)


if __name__ == "__main__":
    main()
