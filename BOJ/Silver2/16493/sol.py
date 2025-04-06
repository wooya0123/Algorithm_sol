N, M = list(map(int, input().split()))  # N일, M개 챕터
chapter_list = [list(map(int, input().split())) for _ in range(M)]
chapter_list.sort(key=lambda x: x[0])

dp = [0] * (N+1)

for day, pages in chapter_list:
    for i in range(N, day-1, -1):
        dp[i] = max(dp[i], dp[i-day]+pages)

print(dp[N])