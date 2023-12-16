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
    repeunit = [1, 1, 1]
    for _ in range(N - 1):
        repeunit.sort()
        if repeunit[0] == repeunit[1] == repeunit[2]:
            repeunit[1] = repeunit[2] = 1
        elif repeunit[0] == repeunit[1]:
            repeunit[1] = 1
        repeunit[0] = repeunit[0] * 10 + 1
    print(sum(repeunit))


if __name__ == "__main__":
    main()
