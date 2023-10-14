import sys
from collections import Counter

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    S = input().strip()

    patterns = []
    for x in range(int(10 ** (N / 2)) + 1):
        num_cnt = [0] * 10
        for n, cnt in Counter(str(x**2)).items():
            num_cnt[int(n)] = cnt
        patterns.append(num_cnt)

    S_cnt = [0] * 10
    for n, cnt in Counter(S).items():
        S_cnt[int(n)] = cnt

    ans = 0
    for p in patterns:
        if S_cnt[0] < p[0]:
            continue
        for i in range(1, 10):
            if S_cnt[i] != p[i]:
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
