from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, Q = map(int, input().split())
    A = list(input().strip())

    cum_A = [0] * (N + 1)

    pre = ""
    for i, a in enumerate(A):
        if pre == a:
            cum_A[i + 1] = cum_A[i] + 1
        else:
            cum_A[i + 1] = cum_A[i]
        pre = a
    debug(cum_A)

    for _ in range(Q):
        l, r = map(int, input().split())
        print(cum_A[r] - cum_A[l])


if __name__ == "__main__":
    main()
