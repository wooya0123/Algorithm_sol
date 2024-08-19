import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]     # 1: N극 2: S극

    move = 0
    # 1은 아래로, 2는 위로
    while move > 0:
        for i in range(99):
            for j in range(100):
                if arr[i+1][j] == 0:    # 움직일 곳이 비어있다면
                    if arr[i][j] == 1:  # 1은 아래로
                        arr[i][j] = 0
                        arr[i+1][j] = 1

                if arr[i-1][j] == 0:    # 움직일 곳이 비어 있다면
                    if arr[i][j] == 2:  # 2는 위로
                        arr[i][j] = 0
                        arr[i-1][j] = 2