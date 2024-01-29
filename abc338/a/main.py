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
    S = input().rstrip()
    if len(S) == 1:
        print("Yes" if S.isupper() else "No")
        return
    print("Yes" if S[0].isupper() and S[1:].islower() else "No")


if __name__ == "__main__":
    main()
