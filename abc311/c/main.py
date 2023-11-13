from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    _ = int(input())
    A = [int(x) - 1 for x in input().split()]

    ans = []
    crr = 0
    visited = set()

    while True:
        if crr in visited:
            break
        visited.add(crr)
        ans.append(crr)
        crr = A[crr]
    ans = ans[ans.index(crr) :]
    print(len(ans))
    print(*[x + 1 for x in ans])


if __name__ == "__main__":
    main()
