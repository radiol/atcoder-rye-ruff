import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    que = deque()
    ans = 0
    for a in A:
        que.append(a)
        while que[-1] - que[0] >= M:
            que.popleft()
        ans = max(ans, len(que))
    print(ans)


if __name__ == "__main__":
    main()
