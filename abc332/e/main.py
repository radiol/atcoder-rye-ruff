from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, D = map(int, input().split())
    W = list(map(int, input().split()))
    total_W = sum(W)
    avg = total_W / D

    dp = [[0.0] * (D + 1) for _ in range(1 << N)]
    for S in range(1 << N):
        y = 0
        for i in range(N):
            if S & (1 << i):
                y += W[i]
        dp[S][1] = (y - avg) ** 2
        for k in range(2, D + 1):
            dp[S][k] = dp[S][k - 1] + dp[0][1]
            T = S
            while T > 0:
                dp[S][k] = min(dp[S][k], dp[S ^ T][k - 1] + dp[T][1])
                T = (T - 1) & S
    print(dp[-1][-1] / D)


if __name__ == "__main__":
    main()
