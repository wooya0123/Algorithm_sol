N, K = list(map(int, input().split()))  # N개 물품, K만큼 버틸 수 있음
stuffs = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)

for W, V in stuffs:
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W]+V)

print(dp[K])