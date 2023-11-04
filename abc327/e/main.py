from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    P = [0, *map(int, input().split())]

    dp = [[float("-inf")] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = P[1]

    for i in range(2, N + 1):
        for j in range(1, i + 1):
            if j == 1:
                dp[i][j] = max(P[i], dp[i - 1][j])
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] * 0.9 + P[i], dp[i - 1][j])
    ans = float("-inf")
    x = 1
    for k in range(1, N + 1):
        rate = dp[-1][k] / x - (1200 / (k**0.5))
        ans = max(ans, rate)
        x = x * 0.9 + 1

    print(ans)


if __name__ == "__main__":
    main()
