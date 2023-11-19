def main():
    N, M = map(int, input().split())
    S = list(input().strip())
    T = list(input().strip())

    dp = [[False] * M for _ in range(N)]
    dp[0][0] = S[0] == T[0]

    for i in range(N - 1):
        for j in range(M):
            if dp[i][j] is False:
                continue
            if S[i + 1] == T[0]:
                dp[i + 1][0] = True
            if j == M - 1:
                for k in range(M):
                    if S[i + 1] == T[k]:
                        dp[i + 1][k] = True
            if S[i + 1] == T[(j + 1) % M]:
                dp[i + 1][(j + 1) % M] = True
    print("Yes" if dp[-1][-1] else "No")


if __name__ == "__main__":
    main()
