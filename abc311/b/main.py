from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, D = map(int, input().split())
    data = [True] * D
    for _ in range(N):
        for i, c in enumerate(input().rstrip()):
            if c == "x":
                data[i] = False
    ans = 0
    cnt = 0
    for d in data:
        if d:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
