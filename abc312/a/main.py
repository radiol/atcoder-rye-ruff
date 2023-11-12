from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = input().strip()
    T = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]
    print("Yes" if S in T else "No")


if __name__ == "__main__":
    main()
