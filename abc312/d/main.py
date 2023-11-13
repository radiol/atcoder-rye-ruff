from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = list(input().strip())
    MOD = 998244353

    # dp[i][j]: i文字目まで見たとき、"("の数-")"の数=j個のときの組み合わせ数
    dp = [[0] * (len(S) + 1) for _ in range(len(S) + 1)]
    dp[0][0] = 1

    for i in range(len(S)):
        for j in range(len(S)):
            match S[i]:
                case "?":
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j - 1] += dp[i][j]
                case "(":
                    dp[i + 1][j + 1] += dp[i][j]
                case ")":
                    dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
            dp[i + 1][j - 1] %= MOD

    print(dp[len(S)][0])


if __name__ == "__main__":
    main()
