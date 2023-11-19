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
    S = [int(i) for i in input().rstrip()]

    ans = zero = one = 0
    for i in range(N):
        if S[i] == 0:
            zero = 1
            one = i
        else:
            zero, one = one, zero + 1
        ans += one
    print(ans)


if __name__ == "__main__":
    main()
