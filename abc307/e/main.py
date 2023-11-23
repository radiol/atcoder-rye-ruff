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
    N, M = (int(x) for x in input().split())
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = M
    for i in range(N - 1):
        dp[i + 1][0] = dp[i][1]
        dp[i + 1][1] = (dp[i][0] * (M - 1) + dp[i][1] * (M - 2)) % MOD
    print(dp[-1][1])


if __name__ == "__main__":
    main()
