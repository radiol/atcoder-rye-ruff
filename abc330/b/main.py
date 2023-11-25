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
    N, L, R = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    ans = []
    for a in A:
        if a < L:
            ans.append(L)
        elif a > R:
            ans.append(R)
        else:
            ans.append(a)
    print(*ans)


if __name__ == "__main__":
    main()
