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
    A = [int(x) for x in input().split()]
    S = input().strip()

    M = [[0] * (1 << 3) for _ in range(N + 1)]
    E = [[0] * (1 << 3) for _ in range(N + 1)]
    X = [[0] * (1 << 3) for _ in range(N + 1)]

    for i, c in enumerate(S):
        for j in range(1 << 3):
            M[i + 1][j] += M[i][j]
            E[i + 1][j] += E[i][j]
            X[i + 1][j] += X[i][j]

        match c:
            case "M":
                M[i + 1][1 << A[i]] += 1
            case "E":
                for j in range(1 << 3):
                    E[i + 1][(1 << A[i]) | j] += M[i][j]
            case "X":
                for j in range(1 << 3):
                    X[i + 1][(1 << A[i]) | j] += E[i][j]

    ans = 0
    for j, x in enumerate(X[N]):
        for k in range(4):
            if (j >> k) & 1 == 0:
                ans += x * k
                break
    print(ans)


if __name__ == "__main__":
    main()
