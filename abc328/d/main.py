from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = input().strip()
    ans = []
    for c in S:
        ans.append(c)
        if ans[-3:] == ["A", "B", "C"]:
            for _ in range(3):
                ans.pop()
    print("".join(ans))


if __name__ == "__main__":
    main()
