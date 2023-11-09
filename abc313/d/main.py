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
    ans = [0] * (N + 1)
    q_cnt = 0
    for i in range(K - 1, N):
        ans[i + 1] = ask(X[: K - 1] + [X[i]])
        q_cnt += 1
    for i in range(K - 1):
        res = ask(X[:i] + X[i + 1 : K + 1])
        q_cnt += 1
        if res == ans[K + 1]:
            ans[i + 1] = ans[K]
        else:
            ans[i + 1] = 1 - ans[K]
    debug(ans)
    debug(q_cnt)

    if sum(ans[1 : K + 1]) % 2 != ans[K]:
        ans = [1 - x for x in ans]

    print(f"! {' '.join(map(str, ans[1:]))}", flush=True)


def ask(x: list[str]) -> int:
    print(f"? {' '.join(x)}", flush=True)
    return int(input())


if __name__ == "__main__":
    main()
