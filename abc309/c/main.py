from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, K = (int(x) for x in input().split())

    events = []
    total = 0
    # M行dataの読み込み
    for _ in range(N):
        a, b = (int(x) for x in input().split())
        events.append((a + 1, b))
        total += b
    events.sort()

    day = 1
    for d, c in events:
        if total <= K:
            break
        day = d
        total -= c
    print(day)


if __name__ == "__main__":
    main()
