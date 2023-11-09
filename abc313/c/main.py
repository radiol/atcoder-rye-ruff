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
    A = list(map(int, input().split()))
    A.sort()
    target = sum(A) // len(A)
    rem = sum(A) % len(A)
    B = [target] * (len(A) - rem) + [target + 1] * rem
    debug(B)
    ans = 0
    for a, b in zip(A, B):
        ans += abs(a - b)
    print(ans // 2)


if __name__ == "__main__":
    main()
