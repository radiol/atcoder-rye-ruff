import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


MOD = 998244353


def main():
    N, X = map(int, input().split())
    T = list(map(int, input().split()))
    # 全体の開始からx秒後に曲nがちょうど終了する確率dp[n][x] ignore
    # X秒までで曲が終了し、X+1秒の時点でどの曲がかかっているかが答えなので0~X+1まで
    dp = [[0] * (X + 2) for _ in range(N)]

    # 1/Nの逆元invを求める
    inv = pow(N, -1, MOD)

    dp[0][0] += 1

    for x in range(X + 1):
        # x秒後にちょうど曲が終わる確率(全ての曲の合計) ignore
        temp_sum = sum(dp[n][x] for n in range(N)) % MOD
        if temp_sum == 0:
            continue
        for n in range(N):
            # 次の曲が終わるのがx+T[n]秒後、x+T[n]>=X+1ならX+1秒後に曲nがかかっている
            next_end = min(X + 1, x + T[n])
            dp[n][next_end] += temp_sum * inv
            dp[n][next_end] %= MOD
    print(dp[0][-1])


if __name__ == "__main__":
    main()
