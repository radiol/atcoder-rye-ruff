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
    _, _ = map(int, input().split())
    S = input().strip()
    C = list(map(int, input().split()))

    group = defaultdict(deque)
    for s, c in zip(S, C):
        group[c].append(s)
    for k in group:
        group[k].appendleft(group[k].pop())
    ans = []
    for c in C:
        s = group[c].popleft()
        ans.append(s)
    print("".join(ans))


if __name__ == "__main__":
    main()
