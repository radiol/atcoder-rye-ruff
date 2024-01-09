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
    n, q = map(int, input().split())
    pos:list[tuple[int, int]] = [(n-i, 0) for i in range(n)]
    for _ in range(q):
        t, c = input().split()
        if t == "1":
            x, y = pos[-1]
            match c:
                case "L":
                    pos.append((x-1, y))
                case "R":
                    pos.append((x+1, y))
                case "U":
                    pos.append((x, y+1))
                case "D":
                    pos.append((x, y-1))
        else:
            p = int(c)
            print(*pos[-p])

if __name__ == "__main__":
    main()
