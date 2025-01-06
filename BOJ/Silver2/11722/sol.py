arr_len = int(input())
arr = list(map(int, input().split()))

# DP 배열 초기화 - 가장 짧은 수열의 길이가 1이므로 1로 초기화
dp = [1] * arr_len

# DP로 가장 긴 감소하는 부분 수열의 길이 계산
for i in range(1, arr_len):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최대 길이 출력
print(max(dp))

# 이전 풀이 - 문제 이해를 잘못 함
# arr_len = input()
# arr = list(map(int, input().split()))
# ans = []
#
# for i in range(len(arr)-1):
#     res = []
#     if arr[i] >= arr[i+1]:
#         res.append(arr[i])
#         for j in range(i+1, len(arr)):
#             if res[-1] > arr[j]:
#                 res.append(arr[j])
#     if len(ans) < len(res):
#         ans = res
#
# print(len(ans) if ans else 1)