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
    A = list(map(int, input().split()))

    cnt = [0] * (N + 1)
    ans = []
    for a in A:
        cnt[a] += 1
        if cnt[a] == 2:
            ans.append(a)

    print(*ans)


if __name__ == "__main__":
    main()
