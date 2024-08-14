import sys
sys.stdin = open('sample_input.txt')

def BFS(start_i, start_j):
    queue = [[start_i, start_j]]
    visited[start_i][start_j] = 1

    while queue:
        current_x, current_y = queue.pop(0)     # 현재 위치
        if arr[current_x][current_y] == 3:
            return visited[current_x][current_y] - 1 - 1
        for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:     # 상하좌우
            next_x = current_x + dx
            next_y = current_y + dy
            if 0 <= next_x < N and 0 <= next_y < N and arr[next_x][next_y] != 1 and visited[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                visited[next_x][next_y] = visited[current_x][current_y] + 1

    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                start_i = i
                start_j = j

    result = BFS(start_i, start_j)
    print(f'#{tc} {result}')






