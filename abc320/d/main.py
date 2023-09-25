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

    edge = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, x, y = map(int, input().split())
        edge[a].append((b, x, y))
        edge[b].append((a, -x, -y))

    visited = set()
    ans = [(0, 0) for _ in range(N + 1)]
    que = deque([(1, 0, 0)])
    while que:
        crr, x, y = que.popleft()
        if crr in visited:
            continue
        visited.add(crr)
        for nxt, dx, dy in edge[crr]:
            if nxt in visited:
                continue
            ans[nxt] = (x + dx, y + dy)
            que.append((nxt, x + dx, y + dy))
    for i in range(1, N + 1):
        if i not in visited:
            print("undecidable")
            continue
        print(*ans[i])


if __name__ == "__main__":
    main()
