from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 998244353


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = input().strip()
    T = input().strip()
    nodes = "ABCDE"
    group_A = set()
    group_B = set()
    for i in range(5):
        group_A.add(nodes[i] + nodes[(i + 1) % 5])
        group_A.add(nodes[i] + nodes[(i - 1) % 5])
        group_B.add(nodes[i] + nodes[(i + 2) % 5])
        group_B.add(nodes[i] + nodes[(i - 2) % 5])
    if S in group_A and T in group_A:
        print("Yes")
        return
    if S in group_B and T in group_B:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
