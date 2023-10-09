def main():
    _ = input()
    S = list(input())

    for i, (a, b, c) in enumerate(zip(S, S[1:], S[2:]), start=1):
        if a + b + c == "ABC":
            print(i)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
