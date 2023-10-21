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


if __name__ == "__main__":
    N = 10
    uf = UnionFind(N)
    # uf:[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    for i in range(N):
        assert uf._get_parent(i) == i
    uf.merge(0, 1)
    uf.merge(3, 2)
    uf.merge(2, 1)
    uf.merge(5, 4)
    uf.merge(5, 6)
    # uf: [[0, 1, 2, 3], [4, 5, 6], [7], [8], [9]]
    assert uf.is_union(0, 3) is True
    assert uf.is_union(4, 6) is True
    assert uf.is_union(0, 6) is False
    print(uf._parent_size)  # [3, 0, 3, -4, 5, -3, 5, -1, -1, -1]
    uf.merge(2, 5)
    print(uf._parent_size)  # [3, 0, 3, -7, 5, 3, 5, -1, -1, -1]
    assert uf.is_union(0, 6) is True
    print(uf._parent_size)  # [3, 0, 3, -7, 5, 3, 3, -1, -1, -1]
    uf.merge(9, 7)
    uf.merge(8, 7)
    # uf: [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]]
    print(uf._parent_size)  # [3, 0, 3, -7, 5, 3, 3, 9, 9, -3]
    assert uf._parent_size == [3, 0, 3, -7, 5, 3, 3, 9, 9, -3]
    assert uf.get_size(3) == 7
    assert uf.get_size(7) == 3
    uf.merge(8, 5)
    # uf: [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    print(uf._parent_size)  # [3, 0, 3, -10, 5, 3, 3, 9, 9, 3]
    assert uf._parent_size == [3, 0, 3, -10, 5, 3, 3, 9, 9, 3]
    assert uf.get_size(7) == 10
    print(uf._parent_size)  # [3, 0, 3, -10, 5, 3, 3, 3, 9, 3]
    assert uf._parent_size == [3, 0, 3, -10, 5, 3, 3, 3, 9, 3]
    print(uf.get_unions())  # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert uf.get_unions() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
