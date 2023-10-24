import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M, P = map(int, input().split())
    print((N - M) // P + 1 if N >= M else 0)


if __name__ == "__main__":
    main()
