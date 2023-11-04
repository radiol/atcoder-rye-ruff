from __future__ import annotations

import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    edge = [set() for _ in range(N + 1)]

    for a, b in zip(A, B):
        if a == b:
            print("No")
            return
        edge[a].add(b)
        edge[b].add(a)

    visited = [-1] * (N + 1)
    que = deque([1])
    visited[1] = 1
    not_used = set(range(1, N + 1))

    while que:
        crr = que.popleft()
        if crr in not_used:
            not_used.remove(crr)
        crr_color = visited[crr]
        for nxt in edge[crr]:
            nxt_color = (crr_color + 1) % 2
            if visited[nxt] == -1:
                visited[nxt] = nxt_color
                que.append(nxt)
            if visited[nxt] != nxt_color:
                print("No")
                return
        if not que and not_used:
            que.append(not_used.pop())
            visited[que[-1]] = 1

    print("Yes")
    debug(visited)


if __name__ == "__main__":
    main()
