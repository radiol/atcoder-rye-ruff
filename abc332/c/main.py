from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    S = list(input().rstrip())
    
    add_logo = 0
    logo = 0
    muji = M
    for c in reversed(S):
        if c == "0":
            logo = add_logo
            muji = M
            continue
        if c == "1":
            if muji > 0:
                muji -= 1
                continue
            if logo > 0:
                logo -= 1
                continue
            add_logo += 1
        if c == "2":
            if logo > 0:
                logo -= 1
                continue
            add_logo += 1
    print(add_logo)


if __name__ == "__main__":
    main()
