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
    B, D = (int(x) for x in input().split())
    if B > D:
        print("Bat")
    else:
        print("Glove")


if __name__ == "__main__":
    main()
