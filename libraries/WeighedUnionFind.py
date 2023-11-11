from __future__ import annotations


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

    # 要素aとbの重みの差を返す. aとbが同じ木に属していない場合はinfを返す
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
