import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    grid = [list(input()) for _ in range(N)]

    cnt = [0] * N
    for i, line in enumerate(grid):
        cnt[i] = -line.count("o")
    result = list(zip(cnt, range(1, N + 1)))
    result.sort()
    print(" ".join([str(idx) for _, idx in result]))


if __name__ == "__main__":
    main()
