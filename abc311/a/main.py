from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = input()
    S = input().rstrip()

    abc = set()
    for i, c in enumerate(S, start=1):
        abc.add(c)
        if len(abc) == 3:
            print(i)
            return


if __name__ == "__main__":
    main()
