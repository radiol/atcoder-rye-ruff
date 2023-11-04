from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())
    C = []
    A = [set()]
    for i in range(1, N + 1):
        c = int(input())
        C.append((c, i))
        A.append(set(map(int, input().split())))
    X = int(input())
    C = [(c, i) for c, i in C if X in A[i]]
    if len(C) == 0:
        print(0)
        print()
        exit()
    C.sort()
    c_first = C[0][0]
    ans = []
    for c, i in C:
        if c != c_first:
            break
        ans.append(i)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
