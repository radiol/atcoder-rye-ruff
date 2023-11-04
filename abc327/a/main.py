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
    S = input().strip()

    for x, y in zip(S, S[1:]):
        if {x, y} == {"a", "b"}:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
