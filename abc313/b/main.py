from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    informations = [list(map(int, input().split())) for _ in range(M)]

    saikyo = set()
    for i in range(1, N + 1):
        for info in informations:
            if i == info[1]:
                break
        else:
            saikyo.add(i)
    print(*saikyo if len(saikyo) == 1 else [-1])


if __name__ == "__main__":
    main()
