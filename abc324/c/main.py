import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, T = input().split()
    N = int(N)

    def check(S: str) -> bool:
        if abs(len(T) - len(S)) > 1:
            return False
        match_cnt = 0
        for t, s in zip(T, S):
            if t != s:
                break
            match_cnt += 1
        for i in range(1, min(len(T), len(S)) + 1):
            if T[-i] != S[-i]:
                break
            match_cnt += 1
        return match_cnt >= min(len(T), len(S)) or (
            len(T) == len(S) and match_cnt >= len(T) - 1
        )

    ans = []
    for i in range(1, N + 1):
        S = input().strip()
        if check(S):
            ans.append(i)
    print(len(ans))
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
