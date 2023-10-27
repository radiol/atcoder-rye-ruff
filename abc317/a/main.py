import sys
from bisect import bisect_left

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, H, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(bisect_left(P, X - H) + 1)


if __name__ == "__main__":
    main()
