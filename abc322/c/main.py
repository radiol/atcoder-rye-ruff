import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    N, _ = map(int, input().split())
    A = [0, *list(map(int, input().split()))]

    ans = [0] * (N + 1)

    nxt_fireworks = A.pop()
    for i in range(N, 0, -1):
        if i == nxt_fireworks:
            ans[i] = 0
            nxt_fireworks = A.pop()
        else:
            ans[i] = ans[i + 1] + 1
    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
