from collections import deque


def main():
    K = int(input())

    que = deque(range(1, 10))
    x = 0
    for _ in range(K):
        x = que.popleft()
        for i in range(x % 10):
            que.append(x * 10 + i)
    print(x)


if __name__ == "__main__":
    main()
