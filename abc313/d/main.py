from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, K = map(int, input().split())
    X = list(map(str, range(1, N + 1)))
    ans = [0] * N
    # x1, x2, ..., xk-1のk-1個とxk~xNのうちから1つの計k個の偶奇を求める
    # これをN-K+1回繰り返す
    for i in range(K - 1, N):
        ans[i] = ask(X[: K - 1] + [X[i]])
    # x1, x2, .... xi-1, xi+1, ...xk+1のk個の偶奇を求める
    # これをK-1回繰り返す
    for i in range(K - 1):
        res = ask(X[:i] + X[i + 1 : K + 1])
        # ans[K]はx1, x2, ..., xk-1, xk+1の偶奇
        # ans[K]と偶奇が一致するなら、xiの偶奇はxkと同じ
        if res == ans[K]:
            ans[i] = ans[K - 1]
        else:
            ans[i] = 1 - ans[K - 1]
    # x1, x2, ... xkの奇数の数がans[K-1]と一致しないなら偶奇を反転させる
    if sum(ans[:K]) % 2 != ans[K - 1]:
        ans = [1 - x for x in ans]

    print(f"! {' '.join(map(str, ans))}", flush=True)


def ask(x: list[str]) -> int:
    print(f"? {' '.join(x)}", flush=True)
    return int(input())


if __name__ == "__main__":
    main()
