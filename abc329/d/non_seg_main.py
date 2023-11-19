def main():
    N, _ = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = [0] * (N + 1)

    top = 0
    for a in A:
        cnt[a] += 1
        if cnt[a] > cnt[top] or (cnt[a] == cnt[top] and a < top):
            top = a
        print(top)


if __name__ == "__main__":
    main()
