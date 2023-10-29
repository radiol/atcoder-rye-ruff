import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 998244353

    inv = pow(N, mod - 2, mod)

    ans = 0
    p = inv
    for a in A:
        ans += a * p
        ans %= mod
        p += p * inv
        p %= mod
    print(ans)


if __name__ == "__main__":
    main()
