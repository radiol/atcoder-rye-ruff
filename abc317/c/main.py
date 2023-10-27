import sys
from itertools import permutations

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())

    d = [[0] * N for _ in range(N)]
    # M行dataの読み込み
    for _ in range(M):
        u, v, c = map(int, input().split())
        d[u - 1][v - 1] = d[v - 1][u - 1] = c

    ans = 0
    for p in permutations(range(N)):
        temp_dist = 0
        for crr, nxt in zip(p, p[1:]):
            if d[crr][nxt] == 0:
                break
            temp_dist += d[crr][nxt]
            ans = max(ans, temp_dist)
    print(ans)


if __name__ == "__main__":
    main()
