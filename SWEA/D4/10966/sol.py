import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 행, M: 열
    map_list = [input() for _ in range(N)]      # W: 물, L: 땅
    visited = [[0] * M for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    res = 0
    queue = []

    for i in range(N):
        for j in range(M):
            if map_list[i][j] == 'L':       # i, j가 시작점
                queue.append((i,j))
                visited[i][j] = 1






    #         if map_list[i][j] == 'W':       # W에서 L로 이동하는 최단거리를 기록하는데 visited에 자기보다 큰 값이 있으면 작은 걸로 갱신
    #             queue.append((i, j, 0))     # 모든 물의 위치 저장
    #             move = 0
    #             visited = [[0] * M for _ in range(N)]
    #             queue = [[i, j]]
    #             visited[i][j] = 1           # W에는 1 기록
    #
    #             while queue:
    #                 ci, cj = queue.pop(0)
    #
    #                 for di, dj in [-1, 0], [1, 0], [0, -1], [0, 1]:     # 상하좌우
    #                     ni = ci + di
    #                     nj = cj + dj
    #                     if 0 <= ni < N and 0 <= nj < M and map_list[ni][nj] != 'W' and visited[ni][nj] == 0:
    #                         if map_list[ni][nj] == 'L':
    #                             queue.append([ni, nj])
    #                             visited[ni][nj] = 1
    #                             if check[ni][nj] == 0:
    #                                 check[ni][nj] = check[ci][cj] + 1
    #                             elif check[ni][nj] > check[ci][cj] + 1:
    #                                 check[ni][nj] = check[ci][cj] + 1
    #
    # for x in range(N):
    #     for y in range(M):
    #         res += check[x][y]
    # print(f'#{tc} {res}')


    while queue:
        ci, cj = queue.pop(0)

        for di, dj in [-1, 0], [1, 0], [0, -1], [0, 1]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if map_list[ni][nj] == 'W':
                    visited[ni][nj] = visited[ci][cj] + 1
                    move = visited[ni][nj]
                    queue = []
                    break
                else:
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[ci][cj] + 1
        res += (move-1)
    print(f'#{tc} {res}')




