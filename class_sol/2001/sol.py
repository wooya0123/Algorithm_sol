import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for k in range(M):
                c = i+k
                for m in range(M):
                    total += arr[c][j+m]
            if max_total < total:
                max_total = total

    print(f'#{tc} {max_total}')




