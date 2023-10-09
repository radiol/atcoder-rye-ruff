def main():
    N, _ = map(int, input().split())
    S = input()
    T = input()

    ans = 0
    is_top_match = T[:N] == S
    is_tail_match = T[-N:] == S

    if not is_tail_match:
        ans += 1
    if not is_top_match:
        ans += 2
    print(ans)


if __name__ == "__main__":
    main()
