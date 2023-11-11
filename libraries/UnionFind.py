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
