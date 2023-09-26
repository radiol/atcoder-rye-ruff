import sys
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())

    ans = [0] * (N + 1)
    members = list(range(1, N + 1))
    heapify(members)
    events = []

    # M行dataの読み込み
    for _ in range(M):
        t, w, s = map(int, input().split())
        heappush(events, (t, 1, w, s))

    while events:
        event = heappop(events)
        if event[1] == 0:
            _, _, n = event
            heappush(members, n)
            continue
        if event[1] == 1 and members:
            t, _, w, s = event
            n = heappop(members)
            ans[n] += w
            heappush(events, (t + s, 0, n))
    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
