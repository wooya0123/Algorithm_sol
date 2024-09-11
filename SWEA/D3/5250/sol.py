import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 표의 가로, 세로
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 0)
    goal = (N-1, N-1)

    for i in range(N):
        for j in range(N):
            x, y = start

            for dx, dy in []