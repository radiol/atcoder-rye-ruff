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
    N, Q = map(int, input().split())
    box = [set() for _ in range(N)]
    for i, c in enumerate(map(int, input().split())):
        box[i].add(c)

    for _ in range(Q):
        a, b = (int(x) - 1 for x in input().split())
        if len(box[a]) > len(box[b]):
            box[a] |= box[b]
            box[b].clear()
            box[a], box[b] = box[b], box[a]
        else:
            box[b] |= box[a]
            box[a].clear()
        print(len(box[b]))


if __name__ == "__main__":
    main()
