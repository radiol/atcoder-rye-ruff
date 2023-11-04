from __future__ import annotations

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(pi[:int(input())+2])

if __name__ == "__main__":
    main()
