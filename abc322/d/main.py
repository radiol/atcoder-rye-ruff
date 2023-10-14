def main():
    minos = []
    for _ in range(3):
        minos.append([list(input()) for _ in range(4)])

    def rotate(mino: list[list]) -> list[list]:
        return [[mino[j][i] for j in range(3, -1, -1)] for i in range(4)]

    m = minos[0]
    for _ in range(5):
        print(*m, sep="\n")
        print()
        m = rotate(m)


if __name__ == "__main__":
    main()
