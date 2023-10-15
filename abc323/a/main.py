import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = [int(x) for i, x in enumerate(input().strip()) if i % 2 == 1]
    print("Yes" if sum(S) == 0 else "No")


if __name__ == "__main__":
    main()
