from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


class WeightedUnionFind:
    # 要素数nで初期化、初めは全て根とする
    # 0-indexなので,1-indexとするときはn+1で初期化する
    # weight_from_parentは親を0とした重みの差を表す
    def __init__(self, n: int) -> None:
        self.length = n
        self._parent_size = [-1] * n
        self._weight_from_parent = [0] * n

    # 要素aが属する木の根と根からの重みを返す
    def _get_parent(self, a: int) -> tuple[int, int]:
        if self._parent_size[a] < 0:
            return a, self._weight_from_parent[a]
        parent, weight = self._get_parent(self._parent_size[a])
        self._parent_size[a] = parent
        self._weight_from_parent[a] += weight
        return self._parent_size[a], self._weight_from_parent[a]

    # 要素aとbを合併する. 既に同じ木に属し、かつ重みが矛盾している場合はFalseを返す
    def merge(self, a: int, b: int, d: int) -> bool:
        x, wx = self._get_parent(a)
        y, wy = self._get_parent(b)
        if x == y:
            return d == wy - wx
        if self._parent_size[x] > self._parent_size[y]:
            x, y = y, x
            wx, wy = wy, wx
            d = -d

        self._parent_size[x] += self._parent_size[y]
        self._parent_size[y] = x
        self._weight_from_parent[y] = wx - wy + d
        return True

    # 要素aとbが同じ木に属するかどうかを返す
    def is_union(self, a: int, b: int) -> bool:
        parent_a, _ = self._get_parent(a)
        parent_b, _ = self._get_parent(b)
        return parent_a == parent_b

    # 要素aとbの重みの差(b-a)を返す. aとbが同じ木に属していない場合はinfを返す
    def diff(self, a: int, b: int) -> int | float:
        parent_a, weight_a = self._get_parent(a)
        parent_b, weight_b = self._get_parent(b)
        if parent_a != parent_b:
            return float("inf")
        return weight_b - weight_a

    # 要素aが属する木の要素数を返す
    def get_size(self, a: int) -> int:
        parent, _ = self._get_parent(a)
        return -self._parent_size[parent]

    # 要素のグループを2次元リストで返す
    def get_unions(self) -> list:
        unions: list = [[] for _ in range(self.length)]
        for i in range(self.length):
            parent, _ = self._get_parent(i)
            unions[parent].append(i)
        return [l for l in unions if len(l) != 0]


def main():
    N, Q = map(int, input().split())

    data = [tuple(map(int, input().split())) for _ in range(Q)]

    S = []
    uf = WeightedUnionFind(N + 1)
    for i, (a, b, d) in enumerate(data, start=1):
        if not uf.merge(a, b, d):
            continue
        S.append(i)
    print(*S)


if __name__ == "__main__":
    main()
