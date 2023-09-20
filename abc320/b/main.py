def main():
    S = input().strip()
    ans = 1
    for i in range(len(S)):
        for j in range(len(S), 0, -1):
            s = S[i:j]
            if s == s[::-1]:
                ans = max(ans, len(s))
    print(ans)


if __name__ == "__main__":
    main()
