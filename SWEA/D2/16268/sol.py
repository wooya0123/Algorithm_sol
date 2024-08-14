import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    dx = [-1, 1, 0, 0]      # 상하좌우
    dy = [0, 0, -1, 1]      # 상하좌우

    max_flowers = 0
    for i in range(N):
        for j in range(M):
            flowers = arr[i][j]         # 현재 위치의 꽃가루를 먼저 더하기
            for k in range(4):          # 이동할 상하좌우의 좌표값 정하기
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:     # 만약 범위 내에 있으면 꽃가루 더하기
                    flowers += arr[nx][ny]
            if max_flowers < flowers:
                max_flowers = flowers               # 꽃가루 합의 최대 구하기
    print(f'#{tc} {max_flowers}')


