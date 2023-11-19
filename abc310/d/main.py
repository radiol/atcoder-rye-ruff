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
    N, T, M = map(int, input().split())

    hates = []
    for _ in range(M):
        a, b = map(int, input().split())
        hates.append(1 << (a - 1) | 1 << (b - 1))

    ans = 0
    teams = []

    def solve(i: int):
        nonlocal ans
        nonlocal teams
        if i == N:
            if len(teams) == T:
                ans += 1
            return
        for j in range(len(teams)):
            for hate in hates:
                if hate & (teams[j] | 1 << i) == hate:
                    break
            else:
                teams[j] |= 1 << i
                solve(i + 1)
                teams[j] ^= 1 << i
        teams.append(1 << i)
        solve(i + 1)
        teams.pop()

    solve(0)
    print(ans)


if __name__ == "__main__":
    main()
