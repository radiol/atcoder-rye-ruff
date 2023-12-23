from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


class UnionFind:
    # 要素数nで初期化、初めは全て根とする
    # 0-indexなので,1-indexとするときはn+1で初期化する
    def __init__(self, n: int) -> None:
        self.length = n
        self._parent_size = [-1] * n

    # 要素aが属する木の根を返す
    def _get_parent(self, a: int) -> int:
        if self._parent_size[a] < 0:
            return a
        self._parent_size[a] = self._get_parent(self._parent_size[a])
        return self._parent_size[a]

    # 要素aとbを合併する
    def merge(self, a: int, b: int) -> None:
        x, y = self._get_parent(a), self._get_parent(b)
        if x == y:
            return
        if self._parent_size[x] > self._parent_size[y]:
            x, y = y, x
        self._parent_size[x] += self._parent_size[y]
        self._parent_size[y] = x

    # 要素aとbが同じ木に属するかどうかを返す
    def is_union(self, a: int, b: int) -> bool:
        return self._get_parent(a) == self._get_parent(b)

    # 要素aが属する木の要素数を返す
    def get_size(self, a: int) -> int:
        return -self._parent_size[self._get_parent(a)]

    # 要素のグループを2次元リストで返す
    def get_unions(self) -> list:
        unions: list = [[] for _ in [0] * self.length]
        for i in range(self.length):
            unions[self._get_parent(i)].append(i)
        return [l for l in unions if len(l) != 0]


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    H, W = (int(x) for x in input().split())
    # x行y列のデータ(x:0~H-1, y:0~W-1)の取得はgrid[x][y]
    # '.'や'#'で表現される文字列のデータの場合
    grid = [list(input().strip()) for _ in range(H)]

    red = set()

    uf = UnionFind(H * W)
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                if i > 0 and grid[i - 1][j] == "#":
                    uf.merge(i * W + j, (i - 1) * W + j)
                if j > 0 and grid[i][j - 1] == "#":
                    uf.merge(i * W + j, i * W + j - 1)
            else:
                red.add((i, j))
    connect_cnt = len(uf.get_unions()) - len(red)

    inv = pow(len(red), -1, MOD)

    ans = 0
    for y, x in sorted(red):
        conection = set()
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            if 0 <= x + dx < W and 0 <= y + dy < H and grid[y + dy][x + dx] == "#":
                conection.add(uf._get_parent((y + dy) * W + x + dx))
        ans += (connect_cnt - len(conection) + 1) * inv
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
