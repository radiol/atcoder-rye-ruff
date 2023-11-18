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
    N, M = map(int, input().split())
    S = list(input().rstrip())
    T = list(input().rstrip())

    good_i = []

    for i in range(N - M + 1):
        for j in range(M):
            if S[i + j] != T[j]:
                break
        else:
            good_i.append(i)

    while good_i:
        i = good_i.pop()
        for j in range(M):
            S[i + j] = "#"
        for new_i in range(i - M - 1, i + M):
            if new_i < 0 or new_i + M - 1 >= N:
                continue
            cnt = 0
            for j in range(M):
                if S[new_i + j] == "#":
                    cnt += 1
                    if cnt == M:
                        break
                    continue
                if S[new_i + j] != T[j]:
                    break
            else:
                good_i.append(new_i)
    print("Yes" if S.count("#") == N else "No")


if __name__ == "__main__":
    main()
