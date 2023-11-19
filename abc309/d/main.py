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
    N1, N2, M = (int(x) for x in input().split())

    edge = [[] for _ in range(N1 + N2)]
    # M行dataの読み込み
    for _ in range(M):
        u, v = (int(x) - 1 for x in input().split())
        edge[u].append(v)
        edge[v].append(u)

    dist = [0] * (N1 + N2)
    visited = {0}
    que = deque([0])
    while que:
        crr = que.popleft()
        for nxt in edge[crr]:
            if nxt in visited:
                continue
            dist[nxt] = dist[crr] + 1
            que.append(nxt)
            visited.add(nxt)

    que.append(N1 + N2 - 1)
    visited.add(N1 + N2 - 1)
    while que:
        crr = que.popleft()
        for nxt in edge[crr]:
            if nxt in visited:
                continue
            dist[nxt] = dist[crr] + 1
            que.append(nxt)
            visited.add(nxt)
    print(max(dist[:N1]) + max(dist[N1:]) + 1)


if __name__ == "__main__":
    main()
