import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A = [a + 1 for a in A]

    def row_cnt(column_num) -> int:
        rows = 1
        length = 0
        for a in A:
            length += a
            if length > column_num:
                length = a
                rows += 1
        return rows

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

    print(meguru_bisect(max(A) - 1, sum(A)) - 1)


if __name__ == "__main__":
    main()
