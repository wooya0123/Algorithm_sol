from collections import deque

M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def test(arr):
    for row in arr:
        if 0 in row:
            return False
    return True

day = 0

while not test(arr):
    day += 1
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1
    if not q:
        day = -1
        break
    else:
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    arr[nx][ny] = 1
print(day)