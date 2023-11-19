from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


# セグメントツリー
# 演算
def segfunc(x, y):
    if x[1] > y[1] or (x[1] == y[1] and x[0] < y[0]):
        return x
    return y


class SegTree:
    # 初期化(元のリスト、単位元、演算)
    def __init__(self, x_list, init, segfunc):
        # 単位元
        self.init = init
        # 演算
        self.segfunc = segfunc
        self.Height = len(x_list).bit_length() + 1
        # 木
        self.Tree = [init] * (2**self.Height)
        # Tree最下段一番左のインデックス番号
        self.num = 2 ** (self.Height - 1)
        # 最下段に要素をセット
        for i in range(len(x_list)):
            self.Tree[2 ** (self.Height - 1) + i] = x_list[i]
        # 上に向かって構築
        for i in range(2 ** (self.Height - 1) - 1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2 * i], self.Tree[2 * i + 1])

    # 参照
    def select(self, k):
        return self.Tree[k + self.num]

    # 更新(k番目(0インデックス),値)
    def update(self, k, x):
        # 最下段のインデックス番号に合わせる
        i = k + self.num
        # 最下段の要素を更新
        self.Tree[i] = x
        # 上に向かって更新
        while i > 1:
            # iが偶数の時
            if i % 2 == 0:
                self.Tree[i // 2] = self.segfunc(self.Tree[i], self.Tree[i + 1])
            # iが奇数の時
            else:
                self.Tree[i // 2] = self.segfunc(self.Tree[i - 1], self.Tree[i])
            i //= 2

    # 区間の処理
    def query(self, l, r):
        # 半開区間[l:r)
        # 下から処理
        # 計算結果　初期値は単位元
        result = self.init
        # 左端　最下段のインデックスに合わせる
        l += self.num
        # 右端　最下段のインデックスに合わせる　後の処理を楽にするため+1しておく
        r += self.num + 1

        while l < r:
            # lが奇数だったら
            if l % 2 == 1:
                # 値を使う
                result = self.segfunc(result, self.Tree[l])
                # 一個右に移動
                l += 1
            # rが奇数だったら
            if r % 2 == 1:
                # 値を使う
                result = self.segfunc(result, self.Tree[r - 1])
            l //= 2
            r //= 2
        # 結果を返す
        return result


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = [int(x) - 1 for x in input().split()]

    seg = SegTree([(x, 0) for x in range(N)], [0, 0], segfunc)

    ans = []
    for a in A:
        idx, cnt = seg.select(a)
        seg.update(a, (idx, cnt + 1))
        ans.append(str(seg.query(0, N)[0] + 1))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
