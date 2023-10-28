import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    X, Y = map(int, input().split())
    if -3 <= Y - X <= 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
