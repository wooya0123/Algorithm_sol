N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
calculation = [list(map(int, input().split())) for _ in range(M)]

# 0부터 i,j까지 사각형의 누적합
prefix = [[0] * (N+1) for _ in range(N+1)]  # 0 패딩

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = (
            arr[i-1][j-1]
            + prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
        )
# print(prefix)

for x1, y1, x2, y2 in calculation:
    result = (
        prefix[x2][y2]
        - prefix[x1-1][y2]
        - prefix[x2][y1-1]
        + prefix[x1-1][y1-1]
    )
    print(result)

# for i in range(N):
#     if i > 0:
#         prefix[i][0] = arr[i][0] + prefix[i-1][N-1]
#     for j in range(1, N):
#         prefix[i][j] = arr[i][j] + prefix[i][j-1]
# print(prefix)
#
# for x1, y1, x2, y2 in calculation:
#     result = prefix[x2-1][y2-1] - prefix[x1-1][y1-2]
#     print(result)

# for cal in calculation:
#     x1, y1, x2, y2 = cal
#     total = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             total += arr[i][j]
#     print(total)