import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    W_X = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for h in range(24):
        temp = 0
        for w, x in W_X:
            if (x + h) % 24 < 9 or (x + h) % 24 > 17:
                continue
            temp += w
        ans = max(ans, temp)
    print(ans)


if __name__ == "__main__":
    main()
