from __future__ import annotations

import sys
from bisect import bisect_left

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    D = int(input())

    l = [x * x for x in range(2 * 10**6 + 1)]

    ans = float("inf")
    for x in l:
        idx = bisect_left(l, D - x)
        ans = min(ans, abs(x + l[idx] - D))
        if idx > 0:
            ans = min(ans, abs(x + l[idx - 1] - D))
    print(ans)


if __name__ == "__main__":
    main()
