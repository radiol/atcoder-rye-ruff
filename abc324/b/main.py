from itertools import product


def main():
    N = int(input())
    for x, y in product(range(61), range(38)):
        if 2**x * 3**y == N:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
