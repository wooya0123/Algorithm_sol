import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 세로 M: 가로
    flag = [input() for _ in range(N)]
    change_color = []
    change_W = 0
    change_B = 0
    change_R = 0

    for i in range(2, N):
        W = B = R = 0
        for j in range(len(flag)):
            if flag[i][j] != 'W':
                W += 1
            if flag[i][j] != 'B':
                B += 1
            else:
                R += 1


