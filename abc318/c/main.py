import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _, D, P = map(int, input().split())
    F = list(map(int, input().split()))
    F.sort(reverse=True)
    total = sum(F)

    ans = total
    ticket = 0
    for f in F:
        if ticket == 0:
            ticket += D
            total += P
        total -= f
        ticket -= 1
        ans = min(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
