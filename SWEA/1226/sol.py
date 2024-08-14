import sys
sys.stdin = open('input.txt')

def DFS(start_i, start_j):
    stack = [[start_i, start_j]]
    visited[start_i][start_j] = 1

    while stack:
        current_x, current_y = stack.pop()
        if arr[current_x][current_y] == 3:
            return 1
        for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
            nx = current_x + dx
            ny = current_y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] == 0:
                stack.append([nx, ny])
                visited[nx][ny] = 1

    return 0

def BFS(start_i, start_j):
    queue = [[start_i, start_j]]
    visited[start_i][start_j] = 1

    while queue:
        current_x, current_y = queue.pop(0)
        if arr[current_x][current_y] == 3:
            return 1
        for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
            nx = current_x + dx
            ny = current_y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1
    return 0


T = 10

for _ in range(1, 11):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j

    # result = DFS(start_i, start_j)
    result = BFS(start_i, start_j)

    print(f'#{tc} {result}')