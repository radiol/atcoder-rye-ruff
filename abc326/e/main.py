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

    P = [0] * N
    P[0] = inv
    for i in range(N - 1):
        P[i + 1] = P[i] + P[i] * inv
        P[i + 1] %= mod
    debug(P)

    ans = 0
    for a, p in zip(A, P):
        ans += a * p
        ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
