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
    N = int(input())
    events = [tuple(map(int, input().split())) for _ in range(N)]
    actions = []
    monster = [0] * (N + 1)
    for t, x in reversed(events):
        if t == 1:
            if monster[x] > 0:
                actions.append(1)
                monster[x] -= 1
            else:
                actions.append(0)
        else:
            monster[x] += 1
    if sum(monster) > 0:
        print(-1)
        return
    ans = 0
    portion = 0
    res = []
    for t, _ in events:
        if t == 1:
            res.append(actions.pop())
            if res[-1]:
                portion += 1
                ans = max(ans, portion)
        else:
            portion -= 1
    print(ans)
    print(*res)


if __name__ == "__main__":
    main()
