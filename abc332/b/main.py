from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    K, G, M = map(int, input().split())
    glass = 0
    mag = 0
    for _ in range(K):
        if glass == G:
            glass = 0
            continue
        if mag == 0:
            mag = M
            continue
        while mag > 0 and glass < G:
            glass += 1
            mag -= 1
    print(glass, mag)


if __name__ == "__main__":
    main()
