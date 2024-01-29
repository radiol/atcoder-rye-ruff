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


def main():
    count = Counter(input().rstrip())
    print(sorted(count.items(), key=lambda x: (-x[1], x[0]))[0][0])


if __name__ == "__main__":
    main()
