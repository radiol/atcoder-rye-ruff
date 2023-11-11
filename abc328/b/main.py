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
    D = [0, *list(map(int, input().split()))]

    cnt = 0
    for i in range(1, N + 1):
        for d in range(1, D[i] + 1):
            if len(set(str(i) + str(d))) == 1:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
