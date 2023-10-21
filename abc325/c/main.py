import sys
from itertools import product

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


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
        unions = [[] for _ in [0] * self.length]
        for i in range(self.length):
            unions[self._get_parent(i)].append(i)
        return [l for l in unions if len(l) != 0]


def main():
    H, W = map(int, input().split())
    # x行y列のデータ(x:0~H-1, y:0~W-1)の取得はgrid[x][y]
    # '.'や'#'で表現される文字列のデータの場合
    grid = [list(input()) for _ in range(H)]

    sensors_cnt = sum(line.count("#") for line in grid)
    debug(sensors_cnt)
    uf = UnionFind(sensors_cnt)
    sensors = {}

    def add_sensor(x: int, y: int):
        sensor_idx = len(sensors)
        sensors[(x, y)] = sensor_idx
        for dx, dy in product((-1, 0, 1), repeat=2):
            if dx == dy == 0:
                continue
            if not 0 <= x + dx < W or not 0 <= y + dy < H:
                continue
            if (x + dx, y + dy) not in sensors:
                continue
            uf.merge(sensor_idx, sensors[(x + dx, y + dy)])

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "#":
                add_sensor(x, y)
    print(len(uf.get_unions()))


if __name__ == "__main__":
    main()
