import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    S = input().strip()

    patterns = defaultdict(int)
    for x in range(int(10 ** (N / 2)) + 1):
        patterns["".join(sorted(str(x**2).zfill(N)))] += 1

    print(patterns["".join(sorted(S.zfill(N)))])


if __name__ == "__main__":
    main()
