from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, S, K = map(int, input().split())
    total = 0
    for _ in range(N):
        p, q = map(int, input().split())
        total += p * q
    if total < S:
        total += K
    print(total)


if __name__ == "__main__":
    main()
