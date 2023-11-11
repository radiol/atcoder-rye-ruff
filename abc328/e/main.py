from __future__ import annotations

import sys
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M, K = map(int, input().split())

    edge = [[] for _ in range(N)]

    for i in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append((v, w, i))
        edge[v].append((u, w, i))

    def calc_cost(p: tuple[int]):
        useful_edge = set(p)

        que = deque()
        que.append(0)
        visited = [False] * N
        visited[0] = True

        res = 0
        while que:
            crr = que.popleft()
            for nxt, w, i in edge[crr]:
                if visited[nxt]:
                    continue
                if i not in useful_edge:
                    continue
                visited[nxt] = True
                res += w
                res %= K
                que.append(nxt)
        if sum(visited) != N:
            return float("inf")
        return res

    ans = float("inf")
    for p in combinations(range(M), N - 1):
        ans = min(ans, calc_cost(p))
    print(ans)


if __name__ == "__main__":
    main()
