from __future__ import annotations

import sys
from collections import deque
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = input().strip()
    if len(S) < 3:
        print(S)
        exit()
    S = "XX" + S
    pre_que = [0, -1]
    heapify(pre_que)
    post_que = deque(range(2, len(S)))

    idx_que = deque([])

    while post_que:
        idx_que.append(post_que.popleft())
        if len(idx_que) < 3:
            continue
        if S[idx_que[0]] + S[idx_que[1]] + S[idx_que[2]] != "ABC":
            heappush(pre_que, -idx_que.popleft())
            continue
        idx_que.clear()
        for _ in range(2):
            idx_que.appendleft(heappop(pre_que) * -1)
    while idx_que:
        heappush(pre_que, -idx_que.popleft())
    pre_que = sorted([-i for i in pre_que])
    print("".join(S[i] for i in pre_que if i not in (0, 1)))


if __name__ == "__main__":
    main()
