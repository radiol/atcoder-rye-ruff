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
    N, P, Q = map(int, input().split())
    D = list(map(int, input().split()))
    print(min(P, min(D) + Q))


if __name__ == "__main__":
    main()
