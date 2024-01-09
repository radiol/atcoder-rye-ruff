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
    grid = [[""] * N for _ in range(N)]
    x, y = 0, 0
    dx, dy = 1, 0
    for i in range(1, N * N):
        grid[y][x] = str(i)
        while (
            x + dx < 0
            or x + dx >= N
            or y + dy < 0
            or y + dy >= N
            or grid[y + dy][x + dx] != ""
        ):
            dx, dy = rotate(dx, dy)
        x += dx
        y += dy
    grid[N // 2][N // 2] = "T"
    print("\n".join(" ".join(row) for row in grid))


def rotate(x, y):
    return y, -x


if __name__ == "__main__":
    main()
