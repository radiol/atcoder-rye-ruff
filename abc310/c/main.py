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
    N = int(input())
    pattern = set()
    ans = 0
    for _ in range(N):
        S = input().strip()
        if S in pattern:
            continue
        ans += 1
        pattern.add(S)
        pattern.add(S[::-1])
    print(ans)


if __name__ == "__main__":
    main()
