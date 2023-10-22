import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, A, B, C = map(int, input().split())

    D = [list(map(int, input().split())) for _ in range(N)]

    hq = []
    heappush(hq, (0, 0))
    marked = [False] * N

    car_times = [float("inf")] * N
    car_times[0] = 0

    while hq:
        t, crr = heappop(hq)
        marked[crr] = True
        for nxt in range(N):
            if marked[nxt]:
                continue
            nxt_t = t + D[crr][nxt] * A
            if nxt_t < car_times[nxt]:
                car_times[nxt] = nxt_t
                heappush(hq, (nxt_t, nxt))

    hq = []
    heappush(hq, (0, N - 1))
    marked = [False] * N
    train_times = [float("inf")] * N
    train_times[N - 1] = 0
    while hq:
        t, crr = heappop(hq)
        marked[crr] = True
        for nxt in range(N):
            if marked[nxt]:
                continue
            nxt_t = t + D[crr][nxt] * B + C
            if nxt_t < train_times[nxt]:
                train_times[nxt] = nxt_t
                heappush(hq, (nxt_t, nxt))

    print(min([c + t for c, t in zip(car_times, train_times)]))


if __name__ == "__main__":
    main()
