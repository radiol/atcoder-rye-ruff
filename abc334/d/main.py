from __future__ import annotations

import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, Q = (int(x) for x in input().split())
    R = [int(x) for x in input().split()]
    R.sort()

    cum = [0] * (N + 1)
    for i, r in enumerate(R):
        cum[i + 1] = cum[i] + r
    debug(cum)

    for _ in range(Q):
        X = int(input())
        print(bisect_right(cum, X) - 1)


if __name__ == "__main__":
    main()
