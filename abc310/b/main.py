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
    # M行dataの読み込み
    P = []
    F = []
    for _ in range(N):
        p, _, *f = map(int, input().split())
        f = set(f)
        P.append(p)
        F.append(f)

    def check(i) -> bool:
        for _j, (p, f) in enumerate(zip(P, F)):
            if P[i] < p and F[i] >= f:
                return True
            if P[i] == p and F[i] > f:
                return True
        return False

    for i in range(N):
        if check(i):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
