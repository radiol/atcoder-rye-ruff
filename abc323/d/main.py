import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

N = int(input())

que = []
cnt = {}
# M行dataの読み込み
for _ in range(N):
    S, C = map(int, input().split())
    cnt[S] = C
    que.append(S)
heapify(que)

ans = 0
while que:
    S = heappop(que)
    C = cnt[S]
    ans += C % 2
    del cnt[S]

    S <<= 1
    C >>= 1
    while C > 0:
        if C & 1 == 1:
            if S not in cnt:
                heappush(que, S)
                cnt[S] = 1
            else:
                cnt[S] += 1
        S <<= 1
        C >>= 1

print(ans)
