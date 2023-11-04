from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    # 数値データの場合
    grid = [list(map(int, input().split())) for _ in range(9)]

    one_nine_set = set(range(1, 10))
    for row in grid:
        if set(row) != one_nine_set:
            print("No")
            return
    for i in range(9):
        if {grid[j][i] for j in range(9)} != one_nine_set:
            print("No")
            return
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if {grid[i + k][j + l] for k in range(3) for l in range(3)} != one_nine_set:
                print("No")
                return
    print("Yes")


if __name__ == "__main__":
    main()
