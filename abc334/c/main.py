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
    N, K = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]

    diff_head = []
    for a, b in zip(A, A[1:]):
        diff_head.append(b - a)
    cum_head = [0] * (len(diff_head) + 1)
    for i, d in enumerate(diff_head):
        cum_head[i + 1] = cum_head[i] + d

    diff_tail = []
    for a, b in zip(A[::-1], A[-2::-1]):
        diff_tail.append(a - b)

    cum_tail = [0] * (len(diff_tail) + 1)
    for i, d in enumerate(diff_tail):
        cum_tail[i + 1] = cum_tail[i] + d

    ans = float("inf")
    for i in range(K // 2 + 1):
        ans = min(ans, cum_head[i] + cum_tail[K // 2 - i])
    print(ans)


if __name__ == "__main__":
    main()
