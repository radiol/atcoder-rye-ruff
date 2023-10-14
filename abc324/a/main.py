def main():
    _ = input()
    print("Yes" if len(set(input().split())) == 1 else "No")


if __name__ == "__main__":
    main()
