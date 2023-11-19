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
    H, W = (int(x) for x in input().split())
    grid = [list(input().strip()) for _ in range(H)]

    snuke = "snuke"

    visited = [[False] * W for _ in range(H)]
    que: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
    visited[0][0] = True
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while que:
        y, x, i = que.popleft()
        for dy, dx in directions:
            ny, nx, ni = y + dy, x + dx, i + 1
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if visited[ny][nx]:
                continue
            if grid[ny][nx] != snuke[ni % 5]:
                continue
            visited[ny][nx] = True
            que.append((ny, nx, ni))
    print("Yes" if visited[-1][-1] else "No")


if __name__ == "__main__":
    main()
