import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    MAX_SIZE = 102
    N = int(input())
    grid = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]

    for _ in range(N):
        A, B, C, D = (int(x) + 1 for x in input().split())

        grid[A][C] += 1
        grid[B][C] -= 1
        grid[A][D] -= 1
        grid[B][D] += 1

    cnt = 0
    for y in range(len(grid)):
        for x in range(len(grid) - 1):
            grid[x + 1][y] += grid[x][y]
    for x in range(len(grid)):
        for y in range(len(grid) - 1):
            grid[x][y + 1] += grid[x][y]
            if grid[x][y + 1] != 0:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
