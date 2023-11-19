from __future__ import annotations

import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = (int(x) for x in input().split())
    P = [int(x) for x in input().split()]

    edge = [[] for _ in range(N + 1)]
    for i, p in enumerate(P, start=2):
        edge[p].append(i)

    insulances = [0] * (N + 1)
    for _ in range(M):
        x, y = (int(x) for x in input().split())
        insulances[x] = max(insulances[x], y + 1)

    ans = 0
    que = deque([1])

    while que:
        crr = que.popleft()
        if insulances[crr] > 0:
            ans += 1
        for nxt in edge[crr]:
            que.append(nxt)
            insulances[nxt] = max(insulances[nxt], insulances[crr] - 1)
    print(ans)


if __name__ == "__main__":
    main()
