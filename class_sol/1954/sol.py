import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # 현재 위치 좌표
    x = 0
    y = 0
    location = [x, y]

    dx = [0, 1, 0, -1]          # 움직일 x축 방향 설정
    dy = [1, 0, -1, 0]          # 움직일 y축 방향 설정
    direction = 0               # 상황에 따라 움직일 방향 결정할 변수

    for i in range(1, N*N + 1): # 작성할 숫자만큼 반복
        arr[x][y] = i           # 현재 위치에 숫자 넣기
        nx = x + dx[direction]  # 다음 위치는 현재 위치 + x축 방향
        ny = y + dy[direction]  # 다음 위치는 현재 위치 + y축 방향

        if nx > N-1 or ny > N-1 or nx < 0 or ny < 0 or arr[nx][ny] != 0:        # 사각형을 벗어나거나 다음 위치가 숫자가 이미 적혀 있으면
            direction = (direction + 1) % 4     # 방향 재설정. 방향은 4번 바꾼 후 다시 처음 방향이므로 4로 나눈 나머지
            nx = x + dx[direction]              # 다음 위치를 재설정한 방향으로 변경
            ny = y + dy[direction]
        x, y = nx, ny
    print(f'#{tc}')
    for n in arr:
        for s in n:
            print(s, end = ' ')
        print()




    # i = 1
    # while i < N*N:
    #     # 오른쪽으로 이동
    #     if y < N -1 and arr[x][y+1] == 0:
    #         while y < N - 1 and arr[x][y+1] == 0:
    #             arr[x][y] = i
    #             i = i + 1
    #             y = y + 1
    #     # 아래로 이동
    #     elif x < N - 1 and arr[x+1][y] == 0:
    #         while x < N - 1 and arr[x][y] == 0 and arr[x+1][y] == 0:
    #             arr[x][y] = i
    #             i = i+1
    #             x = x+1
    #     # 왼쪽으로 이동
    #     elif y > 0 and arr[x][y-1] == 0:
    #         while y > 0 and arr[x][y] == 0 and arr[x][y-1] == 0:
    #             arr[x][y] = i
    #             i = i + 1
    #             x = x - 1
    #     # 위로 이동
    #     elif x > 0 and arr[x-1][y] == 0:
    #         while y > 0 and arr[x][y] == 0 and arr[x-1][y] == 0:
    #             arr[x][y] = i
    #             i = i + 1
    #             x = x - 1
    # print(arr)