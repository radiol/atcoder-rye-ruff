from __future__ import annotations

import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _, _ = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [-int(x) for x in input().split()]
    A.sort()
    B.sort()

    def is_ok(arg):
        # 条件を満たすかどうか.問題ごとに定義
        a = bisect_right(A, arg)
        b = bisect_right(B, -arg)
        return a >= b

    def meguru_bisect(ng, ok):
        """
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        """
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10**9 + 1))


if __name__ == "__main__":
    main()
