import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = int(input())
    A = list(map(int, input().split()))

    tail_cnt = defaultdict(int)
    for a in A:
        tail_cnt[a] += 1
    head_cnt = {key: 0 for key in tail_cnt}

    ans = 0
    total_comb = 0
    tail_cnt[A[0]] -= 1

    def count_comb(a: int) -> int:
        return head_cnt[a] * tail_cnt[a]

    for pre, crr in zip(A, A[1:]):
        diff = -(count_comb(pre) + count_comb(crr))

        head_cnt[pre] += 1
        tail_cnt[crr] -= 1
        diff += count_comb(pre) + count_comb(crr)
        if pre == crr:
            diff //= 2
        total_comb += diff

        ans += total_comb - (count_comb(crr))
    print(ans)


if __name__ == "__main__":
    main()
