import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N: 퍼즐 크기 K: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    start = []
    for i in range(N):
        for j in range(N):
            if puzzle[0][j] == 1:
                start += [[0, j]]
            elif puzzle[i][0] == 1:
                start += [[i, 0]]
            elif puzzle[i-1][j] == 0 and puzzle[i][j] == 1:
                start += [[i, j]]
            elif puzzle[i][j-1] == 0 and puzzle[i][j] == 1:
                start += [[i, j]]
    print(start)

    # for dx, dy in [0,1], [-1,0]:``


