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


# 0-indexの場合、start_index=0とする
def topological_sort(
    out_edges: list[list[int]],
    in_edge_cnt: list[int],
    use_node: set[int],
    start_index=0,
):
    res = []
    # 親がいないnodeをqueに格納する
    que = [
        i
        for i in range(start_index, len(in_edge_cnt))
        if in_edge_cnt[i] == 0 and i in use_node
    ]
    # queを優先度付きキューに変換する
    heapify(que)
    # BFSで探索する
    while que:
        # queの先頭を取り出し、resに格納する
        crr = heappop(que)
        if crr not in use_node:
            continue
        res.append(crr)
        # crrから出ているedgeを削除する
        for nxt in out_edges[crr]:
            in_edge_cnt[nxt] -= 1
            # 親がいなくなったnodeをqueに格納する
            if in_edge_cnt[nxt] == 0:
                heappush(que, nxt)

    return res


def main():
    N = int(input())

    edge = [[] for _ in range(N)]
    r_edge = [[] for _ in range(N)]
    in_edge_cnt = [0] * N
    for post in range(N):
        _, *P = (int(x) - 1 for x in input().split())
        if len(P) == 0:
            continue
        in_edge_cnt[post] = len(P)
        for pre in P:
            edge[pre].append(post)
            r_edge[post].append(pre)

    need_book = {0}
    visited = {0}
    que = deque([0])
    while que:
        crr = que.popleft()
        for nxt in r_edge[crr]:
            if nxt in visited:
                continue
            visited.add(nxt)
            need_book.add(nxt)
            que.append(nxt)

    res = topological_sort(edge, in_edge_cnt, need_book)
    print(*[x + 1 for x in res[:-1]])


if __name__ == "__main__":
    main()
