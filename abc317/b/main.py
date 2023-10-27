import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = int(input())
    A = set(map(int, input().split()))
    print(*set(range(min(A), max(A) + 1)) - A)


if __name__ == "__main__":
    main()
