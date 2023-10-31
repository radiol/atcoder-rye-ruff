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
    D = list(map(int, input().split()))

    center = (sum(D) + 1) // 2
    for m, d in enumerate(D, start=1):
        if d < center:
            center -= d
            continue
        print(m, center)
        exit()


if __name__ == "__main__":
    main()
