N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0] * N

if N < 3:
    print(sum(stairs))

# dp[i]는 해당 계단을 밟았을 때
# 그 전의 계단에서 한 칸 올라온 경우와 2칸 올라온 경우 중 큰 값을 저장
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        jump2 = stairs[i] + dp[i-2]
        jump1 = stairs[i] + stairs[i-1] + dp[i-3]
        dp[i] = max(jump1, jump2)

    print(dp[-1])


# for i in range(1, N-2):
#     select = sorted([[stairs[i], i],[stairs[i+1], i+1],[stairs[i+2], i+2]], key=lambda x : x[0], reverse=True)
#     res.add(select[0][1])
#     res.add(select[1][1])
#
# ans = 0
# for j in res:
#     ans += stairs[j]
#
# print(ans)
