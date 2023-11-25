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
    N, L = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    ans = 0
    for a in A:
        if a >= L:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
