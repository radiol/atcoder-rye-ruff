def main():
    N = list(input())
    print("Yes" if N[::-1] == sorted(N) and len(N) == len(set(N)) else "No")


if __name__ == "__main__":
    main()
