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
    S = input().rstrip()

    del_idx = []
    forward = []
    for i, c in enumerate(S):
        if c == "(":
            forward.append(i)
        if c == ")" and forward:
            f = forward.pop()
            del_idx.append((f, i))
    del_cnt = [0] * (N + 1)
    for f, t in del_idx:
        del_cnt[f] += 1
        del_cnt[t + 1] -= 1

    cnt = 0
    ans = []
    for i in range(N):
        cnt += del_cnt[i]
        if cnt == 0:
            ans.append(S[i])
    print("".join(ans))


if __name__ == "__main__":
    main()
