import sys
from bisect import bisect_left

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    points = [0] * (N + 1)
    cum_add_points = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        S = input().strip()
        not_solved_point = [0] * M
        for j, c in enumerate(S):
            if c == "o":
                points[i] += A[j]
            else:
                not_solved_point[j] = A[j]

        points[i] += i
        not_solved_point.sort(reverse=True)

        for j in range(M):
            cum_add_points[i][j + 1] = cum_add_points[i][j] + not_solved_point[j]

    top_point = max(points)

    for i in range(1, N + 1):
        print(bisect_left(cum_add_points[i], top_point - points[i]))


if __name__ == "__main__":
    main()
