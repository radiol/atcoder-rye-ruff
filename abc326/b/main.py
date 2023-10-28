import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    for i in range(N, 1000):
        s = str(i)
        if int(s[0]) * int(s[1]) == int(s[2]):
            print(i)
            exit()


if __name__ == "__main__":
    main()
