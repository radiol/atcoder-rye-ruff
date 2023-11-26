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
    X, Y = [0], [0]
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    dp = [[float("-inf")] * 2 for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        match X[i]:
            case 0:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + Y[i], dp[i - 1][1] + Y[i])
                dp[i][1] = dp[i - 1][1]
            case 1:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = max(dp[i - 1][0] + Y[i], dp[i - 1][1])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
