import sys
sys.stdin = open('sample_input.txt')

# def dfs(t, location):
#     if t == L:
#         location.pop()
#         return
#
#     x, y = location.pop()
#     if arr[x][y] == 1:
#         for dx, dy in [-1,0], [1,0], [0,-1], [0,1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 2:
#         for dx, dy in [-1,0], [1,0]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 3:
#         for dx, dy in [0,-1], [0,1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 4:
#         for dx, dy in [-1,0], [0,1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 5:
#         for dx, dy in [1,0], [0,1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 6:
#         for dx, dy in [1,0], [0,-1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     elif arr[x][y] == 7:
#         for dx, dy in [-1,0], [0,-1]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 location.append((nx, ny))
#                 possible.append((nx, ny))
#     dfs(t+1, location)

pipe = [[0,0,0,0], [1,1,1,1], [1,1,0,0], [0,0,1,1], [1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]]
opp = [1,0,3,2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(t, x, y, path):
    if t == L:
        return

    visited[x][y] = 1
    path.append((x,y))

    for dr in range(4):
        nx = x + dx[dr]
        ny = y + dy[dr]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and pipe[arr[x][y]][dr] == 1 and pipe[arr[nx][ny]][dr] == 1:
            dfs(t+1, nx, ny, path)
    visited[x][y] = 0

    # if arr[x][y] == 1:
    #     for dx, dy in [-1,0], [1,0], [0,-1], [0,1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 2:
    #     for dx, dy in [-1,0], [1,0]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 3:
    #     for dx, dy in [0,-1], [0,1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 4:
    #     for dx, dy in [-1,0], [0,1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 5:
    #     for dx, dy in [1,0], [0,1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 6:
    #     for dx, dy in [1,0], [0,-1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)
    # elif arr[x][y] == 7:
    #     for dx, dy in [-1,0], [0,-1]:
    #         nx = x + dx
    #         ny = y + dy
    #         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #             dfs(t+1, nx, ny, path)

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))     # N: 행, M: 열, (R, C) 맨홀 뚜껑 위치, L: 시간
    arr = [list(map(int, input().split())) for _ in range(N)]  # 파이프 배열
    visited = [[0] * M for _ in range(N)]
    possible = []
    path = []


    dfs(1, R, C, path)
    print(len(path))



    # cnt = 0
    # for i in range(N):
    #     for j in range(M):
    #         if visited[i][j] == 1:
    #             cnt += 1
    # print(cnt)
