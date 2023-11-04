from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    B = int(input())

    a = 1
    while a**a <= B:
        if a**a == B:
            print(a)
            return
        a += 1
    print(-1)


if __name__ == "__main__":
    main()
