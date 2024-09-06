import sys
sys.stdin = open('in1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 배열 크기, M: 한 번에 잡을 수 있는 파리
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(N):

            res1 = arr[i][j]
            k = 0
            while k < M-1:
                k += 1
                for di, dj in [-k,0], [k,0], [0,-k], [0,k]:     # 상하좌우
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        res1 += arr[ni][nj]
            if res < res1:
                res = res1

            res2 = arr[i][j]
            s = 0
            while s < M-1:
                s += 1
                for di, dj in [-s,s], [s,s], [s,-s], [-s,-s]:     # 대각선
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        res2 += arr[ni][nj]
            if res < res2:
                res = res2
    print(f'#{tc} {res}')