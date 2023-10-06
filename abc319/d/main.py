import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    cumA = [0] * (N + 1)
    for i, a in enumerate(A):
        cumA[i + 1] = cumA[i] + (a + 1)

    def row_cnt(column_num) -> int:
        x = 0
        cnt = 0
        while x < cumA[-1]:
            x = cumA[bisect_right(cumA, x + column_num) - 1]
            cnt += 1
        return cnt

    def is_ok(x) -> bool:
        return row_cnt(x) <= M

    def meguru_bisect(ng, ok) -> int:
        while abs(ok - ng) > 1:
            mid = (ng + ok) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(max(A), cumA[-1]) - 1)


if __name__ == "__main__":
    main()
