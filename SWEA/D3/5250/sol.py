import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 표의 가로, 세로
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (arr[0][0], 0, 0)
    queue = deque()
    queue.append(start)
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1  # 시작점 방문 체크
    visited[N - 1][N - 1] = 1e9  # 목적지에 최대값 세팅

    while queue:
        w, x, y = queue.popleft()

        for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:  # 하, 우
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] <= visited[N - 1][N - 1]:
                temp = 0
                if w >= arr[nx][ny]:                            # 높이가 다음 칸이 더 낮으면 연료 +1
                    temp = visited[x][y] + 1
                else:                                           # 높이가 다음 칸이 더 높으면 연료 +1, 높이만큼 +
                    temp = visited[x][y] + 1 + (arr[nx][ny] - w)

                if visited[nx][ny]:                             # 이미 와 본 칸이라면
                    if visited[nx][ny] > temp:                  # 전에 왔을 때보다 지금 왔을 때 값이 작으면 갱신
                        visited[nx][ny] = temp
                        queue.append((arr[nx][ny], nx, ny))     # 이동할 칸에 넣어주기
                    else:
                        continue
                else:
                    visited[nx][ny] = temp                      # 와본 적이 없는 칸이면 temp값 넣기
                    queue.append((arr[nx][ny], nx, ny))         # 이동할 칸에 추가

    print(f'#{tc} {visited[N - 1][N - 1] - 1}')


