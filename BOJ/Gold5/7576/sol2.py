from collections import deque

M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
zero_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j, 0))
        elif arr[i][j] == 0:
            zero_cnt += 1

max_day = 0
while q and zero_cnt > 0:
    x, y, day = q.popleft()
    max_day = max(max_day, day+1)

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            zero_cnt -= 1
            q.append((nx, ny, day+1))

print(max_day if zero_cnt == 0 else -1)