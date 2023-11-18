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
    _ = int(input())
    S = list(input().rstrip())

    cnt = {c: set() for c in "abcdefghijklmnopqrstuvwxyz"}

    crr_c = " "
    crr_len = 0
    for c in S:
        if crr_c != c:
            crr_c = c
            crr_len = 1

        else:
            crr_len += 1
        cnt[c].add(crr_len)

    print(sum([len(v) for v in cnt.values()]))


if __name__ == "__main__":
    main()
