N = int(input())

dp = [0] * (N+1)
dp[1] = 0

if N > 1:
    dp[2] = 1

for i in range(3, N+1):
    case_one = dp[i-1] + 1

    if i % 2 == 0:
        case_two = dp[i // 2] + 1
    else:
        case_two = 1e9

    if i % 3 == 0:
        case_three = dp[i // 3] + 1
    else:
        case_three = 1e9
    dp[i] = min(case_one, case_two, case_three)

print(dp[N])

