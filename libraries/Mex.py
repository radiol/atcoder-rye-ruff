from __future__ import annotations


class Mex:
    # 内部リストAに対して追加・更新(add, update)を行う
    # 内部リストAのMexを取得
    def __init__(self, max_value: int, a: list[int]) -> None:
        self._max_value = max_value
        self._fenwick_tree = FenwickTree(max_value + 1, [1] * (max_value + 1))
        self._cnt = [0] * (max_value + 1)
        self._A: list[int] = []
        for x in a:
            self.add(x)
        self.size = len(a)

    def add(self, x: int) -> None:
        self._A.append(x)
        if x <= self._max_value:
            self._cnt[x] += 1
            if self._cnt[x] == 1:
                self._fenwick_tree.add(x, -1)

    def update(self, idx: int, x: int) -> None:
        if self._A[idx] <= self._max_value:
            self._cnt[self._A[idx]] -= 1
            if self._cnt[self._A[idx]] == 0:
                self._fenwick_tree.add(self._A[idx], 1)
        self._A[idx] = x
        if x <= self._max_value:
            self._cnt[x] += 1
            if self._cnt[x] == 1:
                self._fenwick_tree.add(x, -1)

    def get_mex(self) -> int:
        result, _ = self._fenwick_tree.lower_bound(1)
        return result


class FenwickTree:
    def __init__(self, n: int, a=None) -> None:
        # 長さn, 初期値0でで配列を初期化する。配列aを与えた場合、aの値で初期化する。
        self.length = n
        self.data = [0] * n
        self.depth = n.bit_length()
        if a is not None:
            for i, item in enumerate(a):
                self.add(i, item)

    def add(self, idx: int, x: int) -> None:
        # 要素a[idx]にxを加算する
        idx += 1
        while idx <= self.length:
            self.data[idx - 1] += x
            idx += idx & -idx

    def update(self, idx: int, x: int) -> None:
        # 要素a[idx]をxに更新する
        self.add(idx, x - self.range_sum(idx, idx + 1))

    def sum(self, r: int) -> int:
        # 半開区間[0:r)の区間和を返す。rは含まない。
        result = 0
        while r > 0:
            result += self.data[r - 1]
            r -= r & -r
        return result

    def range_sum(self, l: int, r: int) -> int:
        # 半開区間[l:r)の区間和を返す。lは含む、rは含まない。
        return self.sum(r) - self.sum(l)

    def lower_bound(self, x: int) -> tuple:
        # 累積和がx以上となる最小のidxとその直前の累積和totalを返す。
        # 配列全体の累積和 < xの場合、idx=配列の長さ、total=配列全体の和を返す。
        total = 0
        idx = 0
        for i in range(self.depth, -1, -1):
            k = idx + (1 << i)
            if k <= self.length and total + self.data[k - 1] < x:
                total += self.data[k - 1]
                idx += 1 << i
        return idx, total
