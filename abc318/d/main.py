import sys
from itertools import combinations

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    D = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        for j, d in enumerate(map(int, input().split()), start=i + 1):
            D[i][j] = d
            D[j][i] = d

    dp = [0] * (1 << N)
    for S in range(1 << N):
        for i, j in combinations(range(N), 2):
            if (S >> i) & 1 == 1 or (S >> j) & 1 == 1:
                continue
            new_S = S + (1 << i) + (1 << j)
            dp[new_S] = max(dp[new_S], dp[S] + D[i][j])
    print(max(dp))


if __name__ == "__main__":
    main()
