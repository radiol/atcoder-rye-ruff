from __future__ import annotations

import sys
from itertools import product

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    HA, WA = (int(x) for x in input().split())
    A = [list(input().rstrip()) for _ in range(HA)]
    HB, WB = (int(x) for x in input().split())
    B = [list(input().rstrip()) for _ in range(HB)]
    HX, WX = (int(x) for x in input().split())
    X = [list(input().rstrip()) for _ in range(HX)]

    total_cnt = sum(row.count("#") for row in A) + sum(row.count("#") for row in B)

    def add(C, sheet, x, y):
        for i, row in enumerate(sheet):
            for j, c in enumerate(row):
                if c == "#":
                    C[y + i][x + j] += 1
        return C

    def check(C):
        cnt = 0
        for i, row in enumerate(X, start=10):
            for j, c in enumerate(row, start=10):
                if c == "#" and C[i][j] == 0:
                    break
                if c == "." and C[i][j] >= 1:
                    break
                cnt += C[i][j]
            else:
                continue
            break
        else:
            return cnt == total_cnt
        return False

    HC = 30
    WC = 30
    for xa, ya, xb, yb in product(
        range(20),
        range(20),
        range(20),
        range(20),
    ):
        C = [[0] * WC for _ in range(HC)]
        C = add(C, A, xa, ya)
        C = add(C, B, xb, yb)
        if check(C):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
