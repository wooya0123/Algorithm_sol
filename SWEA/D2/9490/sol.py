import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 행 M: 열

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flowers = 0
    for i in range(N):
        for j in range(M):
            boom = arr[i][j]

            flowers = boom
            for n in range(1, boom+1):
                for dx, dy in [-n,0], [n,0], [0,-n], [0,n]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        flowers += arr[nx][ny]
            if flowers > max_flowers:
                max_flowers = flowers

    print(f'#{tc} {max_flowers}')


