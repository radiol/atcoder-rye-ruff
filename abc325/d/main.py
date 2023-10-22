import sys
from collections import defaultdict
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())

    entry_times = set()
    exit_times_dict = defaultdict(list)
    for _ in range(N):
        t, d = map(int, input().split())
        entry_times.add(t)
        exit_times_dict[t].append(t + d)
    entry_times = sorted(entry_times)
    entry_times.append(float("inf"))

    hq = []
    ans = 0
    for s, nxt in zip(entry_times, entry_times[1:]):
        crr = s
        for e in exit_times_dict[crr]:
            heappush(hq, e)
        while hq and crr < nxt:
            e = heappop(hq)
            if e >= crr:
                crr += 1
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
