import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 배열 크기 M: 파리채 크기
    flies = [list(map(int, input().split())) for _ in range(N)]

    # 각 좌표를 돌면서 해당 좌표를 왼쪽 코너로 삼고 파리채 크기만큼 조사
    max_fly = 0
    for x in range(N):
        for y in range(N):
            cnt = 0
            for i in range(M):
                for j in range(M):
                    if 0 <= x+i < N and 0 <= y+j < N:       # 가로로 M만큼 조사 -> 아래로 내려가서 반복
                        cnt += flies[x+i][y+j]
            if max_fly < cnt:
                max_fly = cnt

    print(f'#{tc} {max_fly}')
