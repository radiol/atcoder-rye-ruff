from __future__ import annotations

import sys
from fractions import Fraction

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())

    result = []

    # M行dataの読み込み
    for i in range(1, N + 1):
        A, B = (int(x) for x in input().split())
        result.append((Fraction(A, A + B), -i))
    result.sort(reverse=True)

    print(*[-x[1] for x in result], sep=" ")


if __name__ == "__main__":
    main()
