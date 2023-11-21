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
    _ = int(input())
    A = [int(x) for x in input().split()]
    S = input().strip()

    M = [0] * (1 << 3)
    E = [0] * (1 << 3)
    X = [0] * (1 << 3)

    for a, c in zip(A, S):
        match c:
            case "M":
                M[1 << a] += 1
            case "E":
                for j in range(1 << 3):
                    E[(1 << a) | j] += M[j]
            case "X":
                for j in range(1 << 3):
                    X[(1 << a) | j] += E[j]

    ans = 0
    for j, x in enumerate(X):
        for k in range(4):
            if (j >> k) & 1 == 0:
                ans += x * k
                break
    print(ans)


if __name__ == "__main__":
    main()
