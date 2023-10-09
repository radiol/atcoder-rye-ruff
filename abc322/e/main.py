import sys
from itertools import product

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, K, P = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]

    dp = {tuple(p): float("inf") for p in product(range(P + 1), repeat=K)}

    dp[tuple([0 for _ in range(K)])] = 0

    for c in C:
        ep = dp.copy()
        cost, A = c[0], c[1:]
        for k, crr_cost in dp.items():
            nxt = tuple([min(P, k[i] + A[i]) for i in range(K)])
            ep[nxt] = min(ep[nxt], crr_cost + cost)
        dp = ep
    print(dp[tuple([P] * K)] if dp[tuple([P] * K)] != float("inf") else -1)


if __name__ == "__main__":
    main()
