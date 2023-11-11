from __future__ import annotations

import sys

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
        self._weight_from_parent = [0] * n

    # 要素aが属する木の根を返す
    def _get_parent(self, a: int) -> tuple[int, int]:
        if self._parent_size[a] < 0:
            return a, self._weight_from_parent[a]
        parent, weight = self._get_parent(self._parent_size[a])
        self._parent_size[a] = parent
        self._weight_from_parent[a] += weight
        return self._parent_size[a], self._weight_from_parent[a]

    # 要素aとbを合併する
    def merge(self, a: int, b: int, d: int) -> None:
        x, wx = self._get_parent(a)
        y, wy = self._get_parent(b)
        if x == y:
            return
        if self._parent_size[x] > self._parent_size[y]:
            x, y = y, x
            wx, wy = wy, wx
            d = -d

        self._parent_size[x] += self._parent_size[y]
        self._parent_size[y] = x
        self._weight_from_parent[y] = wx - wy + d

    # 要素aとbが同じ木に属するかどうかを返す
    def is_union(self, a: int, b: int) -> bool:
        parent_a, _ = self._get_parent(a)
        parent_b, _ = self._get_parent(b)
        return parent_a == parent_b

    # 要素aが属する木の要素数を返す
    def get_size(self, a: int) -> int:
        parent, _ = self._get_parent(a)
        return -self._parent_size[parent]


def main():
    N, Q = map(int, input().split())

    data = [tuple(map(int, input().split())) for _ in range(Q)]

    S = []
    uf = UnionFind(N + 1)
    for i, (a, b, d) in enumerate(data, start=1):
        if uf.is_union(a, b) is False:
            S.append(i)
            uf.merge(a, b, d)
            continue
        if uf._weight_from_parent[b] - uf._weight_from_parent[a] != d:
            continue
        S.append(i)
    print(*S)


if __name__ == "__main__":
    main()
