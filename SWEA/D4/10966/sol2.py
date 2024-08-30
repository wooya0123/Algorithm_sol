import sys
sys.stdin = open('sample_input.txt')

from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))  # N: 행, M: 열
    # map_list = [input() for _ in range(N)]  # W: 물, L: 땅
    visited = [[-1] * M for _ in range(N)]
    res = 0

    queue = []
    for i in range(N):
        map_list = input()
        for j in range(M):
            if map_list[j] == 'W':  # W에서 L로 이동하는 최단거리를 기록하는데 visited에 자기보다 큰 값이 있으면 작은 걸로 갱신
                queue.append((i, j))
                visited[i][j] = 0  # W에는 1 기록

    while queue:
        ci, cj = queue.pop(0)

        for di, dj in [-1, 0], [1, 0], [0, -1], [0, 1]:  # 상하좌우
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1

    for x in visited:
        res += sum(x)
    print(f'#{tc} {res}')