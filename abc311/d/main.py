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
    H, W = map(int, input().split())
    # x行y列のデータ(x:0~H-1, y:0~W-1)の取得はgrid[x][y]
    # '.'や'#'で表現される文字列のデータの場合
    grid = [list(input().strip()) for _ in range(H)]

    marked = [[False] * W for _ in range(H)]
    visited = set()
    crr = (1, 1)
    que = deque()

    que.append(crr)
    marked[1][1] = True
    visited.add(crr)

    def go(crr: tuple[int, int], dire: tuple[int, int]) -> tuple[int, int]:
        x, y = crr
        dx, dy = dire
        while grid[x + dx][y + dy] == ".":
            x += dx
            y += dy
            marked[x][y] = True
        return (x, y)

    dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while que:
        crr = que.popleft()
        for d in dire:
            next = go(crr, d)
            if next not in visited:
                que.append(next)
                visited.add(next)
    print(sum(sum(x) for x in marked))


if __name__ == "__main__":
    main()
