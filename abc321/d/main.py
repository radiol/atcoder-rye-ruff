from bisect import bisect_right


def main():
    N, M, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    cum_B = [0] * (len(B) + 1)

    for i, b in enumerate(B):
        cum_B[i + 1] = cum_B[i] + b

    ans = 0

    for a in A:
        index = bisect_right(B, P - a)
        ans += cum_B[index] + a * index + P * (M - index)

    print(ans)


if __name__ == "__main__":
    main()
