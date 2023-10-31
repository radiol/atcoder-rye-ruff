from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())

    ice = []
    # M行dataの読み込み
    for _ in range(N):
        f, s = map(int, input().split())
        ice.append((s, f))
    ice.sort()

    sa, fa = ice.pop()
    ans = 0
    while ice:
        s, f = ice.pop()
        if f != fa:
            ans = max(ans, sa + s)
            break
        ans = max(ans, sa + s // 2)
    print(ans)


if __name__ == "__main__":
    main()
