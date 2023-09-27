def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if sum(A[:-1]) >= X:
        print(0)
        return
    if sum(A[1:]) < X:
        print(-1)
        return

    total = sum(A[1:-1])
    for i in range(A[0], A[-1] + 1):
        if total + i >= X:
            print(i)
            return


if __name__ == "__main__":
    main()
