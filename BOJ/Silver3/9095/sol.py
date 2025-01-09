T = int(input())
num = [int(input()) for t in range(T)]
res = 0

# dp에 각 숫자에 대한 경우의 수를 모두 저장
dp = [0] * 11
# 초기값은 직접 계산하여 작성
dp[0] = 1
dp[1] = 2
dp[2] = 4

# 다음 값부터는 이전 값을 토대로 작성
# n의 경우의 수 == (n-1) + 1, (n-2) + 2, (n-3) + 3 로 쪼개서 생각할 수 있음
for i in range(3, 11):
    value = 0
    dp[i] += dp[i-1] + dp[i-2] + dp[i-3]

for n in num:
    print(dp[n-1])