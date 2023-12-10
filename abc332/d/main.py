from __future__ import annotations

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    H, W = map(int, input().split())
    # 数値データの場合
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    counter = defaultdict(int)
    counter[make_tuple(A)] = 0
    que = deque()
    que.append(make_tuple(A))
    while que:
        crr = que.popleft()
        for i in range(H - 1):
            nxt = make_list(crr)
            nxt[i], nxt[i + 1] = nxt[i + 1], nxt[i]
            nxt = make_tuple(nxt)
            if nxt in counter:
                continue
            counter[nxt] = counter[crr] + 1
            que.append(nxt)
        for i in range(W - 1):
            nxt = make_list(crr)
            for j in range(H):
                nxt[j][i], nxt[j][i + 1] = nxt[j][i + 1], nxt[j][i]
            nxt = make_tuple(nxt)
            if nxt in counter:
                continue
            counter[nxt] = counter[crr] + 1
            que.append(nxt)
    B = make_tuple(B)
    if B in counter:
        print(counter[B])
    else:
        print(-1)


def make_tuple(A):
    return tuple(tuple(row) for row in A)


def make_list(A):
    return [list(row) for row in A]


if __name__ == "__main__":
    main()
