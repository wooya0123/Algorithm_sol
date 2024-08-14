import sys
sys.stdin = open('sample_input.txt')



'''
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
'''

def search(x, y):
    stack = [[x, y]]
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 좌표가 범위를 벗어나지 않고 벽이 아니고 방문하지 않았는지
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] != 1:
                if arr[nx][ny] == 3:
                    return 1    # 다음 위치가 출구면 1 반환 후 함수 종료
                # 3이 아니라면
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
    
    print(f'#{tc} {search(*start)}')
