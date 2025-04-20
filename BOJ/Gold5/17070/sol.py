from collections import deque

N = int(input())    # 집 크기
arr = [list(map(int, input().split())) for _ in range(N)]

# 오른쪽 이동 여부
def right_possible(i, j):
    if j+1 < N and arr[i][j+1] == 0:
        return True
    else:
        return False
# 아래 이동 여부
def down_possible(i, j):
    if i+1 < N and arr[i+1][j] == 0:
        return True
    else:
        return False
# 대각선 이동 여부
def cross_possible(i, j):
    if i+1 < N and j+1 < N and arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] == 0:
        return True
    else:
        return False

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  # 가로, 세로, 대각선
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        # 파이프가 가로
        if dp[i][j][0] > 0 and right_possible(i, j):
            dp[i][j + 1][0] += dp[i][j][0]  # 가로 -> 가로
        # 파이프가 세로
        if dp[i][j][1] > 0 and down_possible(i, j):
            dp[i + 1][j][1] += dp[i][j][1]  # 세로 -> 세로
        # 파이프가 대각선
        if dp[i][j][2] > 0:
            if right_possible(i, j):
                dp[i][j + 1][0] += dp[i][j][2]  # 대각선 -> 가로
            if down_possible(i, j):
                dp[i + 1][j][1] += dp[i][j][2]  # 대각선 -> 세로

        # 모든 경우 대각선 무빙
        if cross_possible(i, j):
            # 가로 -> 대각선
            dp[i + 1][j + 1][2] += dp[i][j][0]
            # 세로 -> 대각선
            dp[i + 1][j + 1][2] += dp[i][j][1]
            # 대각선 -> 대각선
            dp[i + 1][j + 1][2] += dp[i][j][2]

# print(dp)
res = sum(dp[N-1][N-1])
print(res)