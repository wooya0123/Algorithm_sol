import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    cnt = 0

    k = -1
    for i in range(N//2, -1, -1):
        k += 1
        for j in range(k, N-k):
            if k == 0:
                cnt += farm[i][j]
            else:
                cnt += farm[i][j]
                cnt += farm[N-1-i][j]
    print(f'#{tc} {cnt}')
