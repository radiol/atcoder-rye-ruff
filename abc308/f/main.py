from __future__ import annotations

import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _, _ = (int(x) for x in input().split())
    P = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    D = [int(x) for x in input().split()]

    P.sort()
    L_D = list(zip(L, D))
    L_D.sort(reverse=True)

    que = []
    discount = 0
    for p in P:
        while L_D and L_D[-1][0] <= p:
            _, d = L_D.pop()
            heappush(que, -d)
        if que:
            discount += heappop(que)
    print(sum(P) + discount)


if __name__ == "__main__":
    main()
