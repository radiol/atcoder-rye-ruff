import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    S = input().strip()

    players = {
        "tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481,
    }
    print(players[S])


if __name__ == "__main__":
    main()
