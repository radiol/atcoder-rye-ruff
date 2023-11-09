from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = int(input())
    P = list(map(int, input().split()))
    max_P = max(P)
    print(max_P - P[0] + 1 if max_P != P[0] or P.count(max_P) != 1 else 0)


if __name__ == "__main__":
    main()
