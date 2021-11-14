import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N 물품수, M 무게
items = [map(int, input().split()) for _ in range(N)]  # V 무게 C 만족도 K 물건개수

dp = [0 for _ in range(M+1)]

for i in range(N):
    v, c, k = items[i]
    t = 1
    temp = 0
    while k>0:
        temp = min(k, t)
        for j in range(M, v*temp, -1):
            dp[j] = max(dp[j - v*temp] + c*temp, dp[j])
        t *= 2
        k -= temp

ans = 0
for i in range(M):
    ans = max(dp[i], ans)
print(ans)
