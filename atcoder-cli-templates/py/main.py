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
    N = int(input())
    N, M = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]

    # M行dataの読み込み
    for _ in range(M):
        u, v = (int(x) for x in input().split())

    H, W = (int(x) for x in input().split())
    # x行y列のデータ(x:0~H-1, y:0~W-1)の取得はgrid[x][y]
    # '.'や'#'で表現される文字列のデータの場合
    grid = [list(input().strip()) for _ in range(H)]
    # 数値データの場合
    grid = [[int(x) for x in input().split()] for _ in range(H)]


if __name__ == "__main__":
    main()
