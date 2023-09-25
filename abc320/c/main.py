def main():
    M = int(input())
    S = [[int(i) for i in input()] for _ in range(3)]

    ans = float("inf")
    for i in range(M * 3):
        for j in range(M * 3):
            for k in range(M * 3):
                if (
                    i != j
                    and j != k
                    and k != i
                    and S[0][i % M] == S[1][j % M] == S[2][k % M]
                ):
                    ans = min(ans, max(i, j, k))

    print(ans if ans != float("inf") else -1)


if __name__ == "__main__":
    main()
