from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, X = map(int, input().split())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        if s <= X:
            ans += s
    print(ans)


if __name__ == "__main__":
    main()
