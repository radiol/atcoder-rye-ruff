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
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_A = 10**9
    for q, a in zip(Q, A):
        if a == 0:
            continue
        max_A = min(max_A, q // a)
    ans = 0
    for i in range(max_A + 1):
        max_B = float("inf")
        for q, a, b in zip(Q, A, B):
            if b == 0:
                continue
            max_B = min(max_B, (q - a * i) // b)
        ans = max(ans, i + max_B)
    print(ans)


if __name__ == "__main__":
    main()
