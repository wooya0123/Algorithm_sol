N = int(input())
honey_list = list(map(int, input().split()))

# 좌측 누적 합 및 우측 누적 합 계산
left_sum = [0] * N
right_sum = [0] * N
left_sum[0] = honey_list[0]
right_sum[N - 1] = honey_list[N - 1]

for i in range(1, N):
    left_sum[i] = left_sum[i - 1] + honey_list[i]
for i in range(N - 2, -1, -1):
    right_sum[i] = right_sum[i + 1] + honey_list[i]

# 최대 꿀 계산
max_honey = 0

# case1: 벌(왼쪽 끝) - 벌 - 꿀(오른쪽 끝)
for i in range(1, N - 1):
    honey = (left_sum[N - 1] - honey_list[0] - honey_list[i]) + (right_sum[i + 1])
    max_honey = max(max_honey, honey)

# case2: 벌(왼쪽 끝) - 꿀 - 벌(오른쪽 끝)
for i in range(1, N - 1):
    honey = (left_sum[i] - honey_list[0]) + (right_sum[i] - honey_list[N - 1])
    max_honey = max(max_honey, honey)

# case3: 꿀(왼쪽 끝) - 벌 - 벌(오른쪽 끝)
for i in range(1, N - 1):
    honey = (left_sum[i - 1]) + (right_sum[0] - honey_list[N - 1] - honey_list[i])
    max_honey = max(max_honey, honey)

print(max_honey)
