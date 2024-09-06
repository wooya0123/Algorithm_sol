import sys
sys.stdin = open('sample_input.txt')

def DFS(i,j):
    stack = [0] * (N * 2 - 2)
    stack[0] = (i, j)
    val_lst = [arr[i][j]]
    change_dir = [[1,-1], [1,1], [-1,1], [-1,-1]]
    n = 0
    k = 0
    while stack:
        x, y = stack[k]
        visited[x][y] = 1

        dx, dy = change_dir[n]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] not in val_lst:
                    visited[nx][ny] = 1
                    k += 1
                    stack[k] = (nx, ny)
                    val_lst.append(arr[nx][ny])
                else:
                    n += 1
        else:
            n += 1

        if n >= 5:
            return False
        if (nx, ny) == (i, j):
            return len(val_lst)

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 격자 크기 N * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N-2):
        for j in range(N-2):
            DFS(i, j)
