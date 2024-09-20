# import sys
# sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N x N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    startpoint = [[0] * N for _ in range(N)]

    ans = -1
    start = 1e9


    for i in range(N):
        for j in range(N):
            # 한 출발점에서 확인해본 곳들은 출발지점으로 삼아도 같은 결과이므로 확인 X
            cnt = 1
            if startpoint[i][j] == 0:
                startpoint[i][j] = 1
                temp = arr[i][j]

                # visited = [[0] * N for _ in range(N)]
                queue = deque()
                queue.append((i, j))

                while queue:
                    i, j = queue.popleft()

                    for di, dj in [-1,0], [1,0], [0,-1], [0,1]:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == arr[i][j] + 1:
                                cnt += 1
                                queue.append((ni, nj))
                                startpoint[ni][nj] = 1
                if ans < cnt:
                    ans = cnt
                    start = temp
                elif ans == cnt:
                    if start > temp:
                        start = temp


    print(f'#{tc} {start} {ans}')


