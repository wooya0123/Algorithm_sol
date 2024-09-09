from collections import deque

import sys
sys.stdin = open('sample_input.txt')

def bfs(x, y):
    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0],
            [1, 0, 1, 0]]  # 파이프 연결 상황
    opp = [1, 0, 3, 2]  # 반대 방향 체크

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited = [[0] * M for _ in range(N)]
    ans = 0             # 체크한 곳 갯수 세기

    q.append((x, y))    # 시작점 넣고 시작
    visited[x][y] = 1   # 1시간 후에 맨홀
    ans += 1

    while q:
        cx, cy = q.popleft()
        if visited[cx][cy] == L:
            return ans
        for dr in range(4):
            nx = cx + dx[dr]
            ny = cy + dy[dr]
            # 현재 파이프에서 다음 파이프 봤을 때 연결됐는지, 다음 파이프 입장에서 현재 파이프와 연결됐는지 확인
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and pipe[arr[cx][cy]][dr] == 1 and pipe[arr[nx][ny]][opp[dr]] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                ans += 1
    return ans

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))     # N: 행, M: 열, (R, C) 맨홀 뚜껑 위치, L: 시간
    arr = [list(map(int, input().split())) for _ in range(N)]  # 파이프 배열

    ans = bfs(R, C)
    print(f'#{tc} {ans}')