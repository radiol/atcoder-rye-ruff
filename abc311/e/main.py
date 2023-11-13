from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    H, W, N = map(int, input().split())
    grid = (
        [[False] * (W + 2)]
        + [[False] + [True] * W + [False] for _ in range(H)]
        + [[False] * (W + 2)]
    )
    for _ in range(N):
        a, b = map(int, input().split())
        grid[a][b] = False
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        if grid[i][1]:
            dp[i][1] = 1
    for j in range(1, W + 1):
        if grid[1][j]:
            dp[1][j] = 1

    for i in range(2, H + 1):
        for j in range(2, W + 1):
            if not grid[i][j]:
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    print(sum(sum(x) for x in dp))


if __name__ == "__main__":
    main()
