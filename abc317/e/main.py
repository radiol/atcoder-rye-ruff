import sys
from collections import deque
from itertools import product

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
    grid = [["#", *list(input().strip()), "#"] for _ in range(H)]
    grid = [["#"] * len(grid[0]), *grid, ["#"] * len(grid[0])]

    S = (-1, -1)
    G = (-1, -1)
    for y, x in product(range(1, H + 1), range(1, W + 1)):
        match grid[y][x]:
            case ">":
                i = 1
                while grid[y][x + i] in ".!":
                    grid[y][x + i] = "!"
                    i += 1
            case "<":
                i = 1
                while grid[y][x - i] in ".!":
                    grid[y][x - i] = "!"
                    i += 1
            case "v":
                i = 1
                while grid[y + i][x] in ".!":
                    grid[y + i][x] = "!"
                    i += 1
            case "^":
                i = 1
                while grid[y - i][x] in ".!":
                    grid[y - i][x] = "!"
                    i += 1
            case "S":
                S = (y, x)
            case "G":
                G = (y, x)

    dist = [[-1] * len(grid[0]) for _ in range(len(grid))]
    dist[S[0]][S[1]] = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    que = deque([S])
    while que:
        y, x = que.popleft()
        for dy, dx in directions:
            new_y = y + dy
            new_x = x + dx
            if grid[new_y][new_x] not in ".SG":
                continue
            if dist[new_y][new_x] != -1:
                continue
            dist[new_y][new_x] = dist[y][x] + 1
            que.append((new_y, new_x))
    print(dist[G[0]][G[1]])


if __name__ == "__main__":
    main()
