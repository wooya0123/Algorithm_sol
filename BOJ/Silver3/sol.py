N = int(input())
stairs = [int(input()) for _ in range(N)]




# dp[0] = stairs[0]
# dp[1] = stairs[0] + stairs[1]
# dp[2] = max(stairs[0] + stairs[1], stairs[0] + stairs[2])
#
# for i in range(3, N):
#     dp[i] = max(dp[i-1] + stairs[i-2] + stairs[i-1], dp[i-1] + stairs[i-2] + stairs[i])

dp = [0] * N
dp[0] = stairs[0]
res = stairs[0]

for i in range(1, N-1, 2):
    if dp[N-1]:
        pass
    else:
        break
    next = max(stairs[i], stairs[i+1])
    total = dp[i-1] + next
    dp[i], dp[i+1] = total, total
dp[-1] = dp[-2]