import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N: 퍼즐 크기 K: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        row = col = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                row += 1
            else:
                if row == K:
                    result += 1
                row = 0
            if puzzle[j][i] == 1:
                col += 1
            else:
                if col == K:
                    result += 1
                col = 0
        if row == K:
            result += 1
        if col == K:
            result += 1
    print(f'#{tc} {result}')