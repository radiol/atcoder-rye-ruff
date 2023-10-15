import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def debug(*args, sep=None):
    if sep is None and hasattr(args[0], "__iter__"):
        sep = "\n"
    print("Debug:", *args, file=sys.stderr, sep=sep)


def main():
    N, T = input().split()
    N = int(N)
    T = T.strip()

    forward_match_cnt = [0] * (len(T) + 1)
    backward_match_cnt = [0] * (len(T) + 1)

    forward_match_cnt[0] = backward_match_cnt[0] = N

    for _ in range(N):
        S = input().strip()
        idx = 0
        for s in S:
            if s == T[idx]:
                idx += 1
                forward_match_cnt[idx] += 1
            if idx >= len(T):
                break

        idx = 1
        for s in reversed(S):
            if s == T[len(T) - idx]:
                backward_match_cnt[idx] += 1
                idx += 1
            if idx > len(T):
                break
        # debug(forward_match_cnt)
        # debug(backward_match_cnt)

        last_backward = 0
        ans = 0
        for f, b in zip(forward_match_cnt, reversed(backward_match_cnt)):
            cnt = f * (b - last_backward)
            if cnt != 0:
                ans += cnt
                last_backward = b
    print(ans)


if __name__ == "__main__":
    main()
