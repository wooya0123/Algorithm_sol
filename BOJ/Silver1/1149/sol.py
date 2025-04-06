N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

min_cost = 1e9

for i in range(3):
    dp = [0] * N
    dp[0] = costs[0][i]
    color = i
    for j in range(1, N):
        cost = 0
        if color == 0:
            if costs[j][1] > costs[j][2]:
                cost = costs[j][2]
                color = 2
            else:
                cost = costs[j][1]
                color = 1
        elif color == 1:
            if costs[j][0] > costs[j][2]:
                cost = costs[j][2]
                color = 2
            else:
                cost = costs[j][0]
                color = 0
        elif color == 2:
            if costs[j][0] > costs[j][1]:
                cost = costs[j][1]
                color = 1
            else:
                cost = costs[j][0]
                color = 0

        dp[j] = cost + dp[j-1]

    if min_cost > dp[-1]:
        min_cost = dp[-1]

print(min_cost)



