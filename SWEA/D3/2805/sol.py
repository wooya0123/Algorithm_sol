import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    cnt = 0

    k = -1
    for i in range(N//2, -1, -1):       # 중간 행부터 시작
        k += 1                          # 열 조절하기 위한 k
        for j in range(k, N-k):         # 열 범위
            if k == 0:                  # 중간 행일 경우 한 번만 더하기
                cnt += farm[i][j]
            else:                       # 그 외 행일 경우 반대편도 더하기
                cnt += farm[i][j]
                cnt += farm[N-1-i][j]
    print(f'#{tc} {cnt}')