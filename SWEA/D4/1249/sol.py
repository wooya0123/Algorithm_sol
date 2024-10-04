from collections import deque           # deque 써놓고 import 안 넣어서 계속 런타임 발생했음....
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())        # 지도 크기 N x N
    arr = [list(map(int, input())) for _ in range(N)]   # 지도
    visited = [[1e9] * N for _ in range(N)]     # 최소 복구 시간을 기록할 예정이므로 초기 값을 매우 크게 설정
    visited[0][0] = 0

    # BFS 탐색, visited의 각 칸에 최소 복구 시간을 기록하면서 가기
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for dx, dy in [-1,0], [1,0], [0,-1], [0,1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                temp = visited[x][y] + arr[nx][ny]      # 이동할 곳에 기록할 누적 복구 시간
                if visited[N-1][N-1] != 1e9:            # 만약 도착지에 한 번 도달했다면 그 값보다 지금 기록할 누적 복구 시간이 크면 안 봐도 됨
                    if visited[N-1][N-1] < temp:
                        continue
                if visited[nx][ny] > temp:              # 이동할 곳에 값이 저장돼 있는데 기록할 값보다 크다면 작은 값으로 갱신
                    visited[nx][ny] = temp
                    q.append((nx, ny))

    print(f'#{tc} {visited[N-1][N-1]}')
