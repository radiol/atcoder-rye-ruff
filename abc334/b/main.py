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
    A, M, L, R = map(int, input().split())
    L -= A
    R -= A
    print(R // M - (L - 1) // M)


if __name__ == "__main__":
    main()
