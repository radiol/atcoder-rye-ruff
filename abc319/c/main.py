from __future__ import annotations

import sys
from itertools import permutations


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    C = []
    for _ in range(3):
        C.extend(list(map(int, input().strip().split())))

    def check(p: tuple[int, ...]) -> bool:
        number_counter_dict = create_patterns_dict()
        for n in range(9):
            idx = p.index(n)
            for key, stack in number_counter_dict.items():
                if idx not in key:
                    continue
                stack.append(C[idx])
                if len(stack) == 2 and stack[0] == stack[1]:
                    return False
        return True

    cnt = 0
    for p in permutations(range(9)):
        if check(p):
            cnt += 1
    print(cnt / (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9))


def create_patterns_dict() -> dict:
    return {
        (0, 1, 2): [],
        (3, 4, 5): [],
        (6, 7, 8): [],
        (0, 3, 6): [],
        (1, 4, 7): [],
        (2, 5, 8): [],
        (0, 4, 8): [],
        (2, 4, 6): [],
    }


if __name__ == "__main__":
    main()
