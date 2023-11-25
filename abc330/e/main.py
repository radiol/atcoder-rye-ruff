from __future__ import annotations

import sys
from collections import Counter

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


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
        assert l <= r
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


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = Counter(A)

    MAX = 2 * 10**5

    mex = FenwickTree(MAX + 1, [1] * (MAX + 1))
    for a in A:
        if a > MAX:
            continue
        if mex.range_sum(a, a + 1) == 0:
            continue
        mex.add(a, -1)

    ans = []
    for _ in range(Q):
        i, x = map(int, input().split())
        i -= 1
        a = A[i]
        A[i] = x
        cnt[a] -= 1
        if x not in cnt:
            cnt[x] = 0
        cnt[x] += 1

        if a <= MAX and cnt[a] == 0:
            mex.update(a, 1)
        if x <= MAX and cnt[x] == 1:
            mex.update(x, 0)
        idx, _ = mex.lower_bound(1)
        ans.append(idx)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
