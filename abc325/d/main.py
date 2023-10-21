import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N = int(input())

    entry_exit_times = []
    for _ in range(N):
        t, d = map(int, input().split())
        entry_exit_times.append((t, t + d))
    entry_exit_times.sort(reverse=True)

    exit_times = []
    now = 0
    ans = 0
    while entry_exit_times:
        s, e = entry_exit_times.pop()
        now = max(now, s)
        heappush(exit_times, e)
        while exit_times:
            while entry_exit_times and entry_exit_times[-1][0] <= now:
                _, e = entry_exit_times.pop()
                heappush(exit_times, e)
            e = heappop(exit_times)
            if e >= now:
                ans += 1
                now += 1
    print(ans)


if __name__ == "__main__":
    main()
