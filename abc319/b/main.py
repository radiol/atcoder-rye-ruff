def main():
    N = int(input())
    div = [i for i in range(1, 10) if N % i == 0]
    div.sort()
    ans = []
    for i in range(N + 1):
        for j in div:
            if i % (N // j) == 0:
                ans.append(j)
                break
        else:
            ans.append("-")
    print(*ans, sep="")


if __name__ == "__main__":
    main()
