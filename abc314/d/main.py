from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = int(input())
    S = list(input().strip())
    Q = int(input())

    big_flag = False
    small_flag = False
    default_index = set()

    for _ in range(Q):
        t, x, c = input().strip().split()
        t = int(t)
        x = int(x) - 1
        match t:
            case 1:
                S[x] = c
                default_index.add(x)
            case 2:
                small_flag = True
                big_flag = False
                default_index.clear()
            case 3:
                big_flag = True
                small_flag = False
                default_index.clear()
    if small_flag:
        S = [c if i in default_index else c.lower() for i, c in enumerate(S)]
    if big_flag:
        S = [c if i in default_index else c.upper() for i, c in enumerate(S)]
    print("".join(S))


if __name__ == "__main__":
    main()
