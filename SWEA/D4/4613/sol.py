import sys
sys.stdin = open('sample_input.txt')

def check_rect(arr, x, y, color):
    cnt = 0
    for r in range(x, y):           # 행 범위 내에서 열 탐색하면서 color랑 같지 않으면 색칠
        for c in range(M):
            if arr[r][c] != color:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    W = B = R = 0
    ans = N * M                     # 최대 색칠 횟수
    for i in range(1, N - 1):       # W 범위
        for j in range(i + 1, N):   # B 범위
            # 0, i
            S = check_rect(flag, 0, i, 'W')
            # i, j
            S += check_rect(flag, i, j, 'B')
            # j, N
            S += check_rect(flag, j, N, 'R')

            ans = min(ans, S)

    print(f'#{tc} {ans}')

