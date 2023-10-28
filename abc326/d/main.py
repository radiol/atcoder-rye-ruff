import sys
from itertools import permutations

sys.setrecursionlimit(10**6)


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    R = list(input())
    C = list(input())

    def check(G: list[list]):
        row_head = []
        for line in G:
            for c in line:
                if c != ".":
                    row_head.append(c)
                    break
        column_head = []
        for x in range(N):
            for y in range(N):
                if G[y][x] != ".":
                    column_head.append(G[y][x])
                    break
        return row_head == R and column_head == C

    for A_pattern in permutations(range(N)):
        for B_pattern in permutations(range(N)):
            for C_pattern in permutations(range(N)):
                flag = True
                for a, b, c in zip(A_pattern, B_pattern, C_pattern):
                    if a == b or b == c or c == a:
                        flag = False
                        break
                if flag is False:
                    continue
                G = [["."] * N for _ in range(N)]
                for y, x in enumerate(A_pattern):
                    G[y][x] = "A"
                for y, x in enumerate(B_pattern):
                    G[y][x] = "B"
                for y, x in enumerate(C_pattern):
                    G[y][x] = "C"

                if check(G):
                    print("Yes")
                    for line in G:
                        print(*line, sep="")
                    exit()
    print("No")


if __name__ == "__main__":
    main()
