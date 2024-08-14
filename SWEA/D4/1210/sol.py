import sys
sys.stdin = open('input.txt')
T = 10

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = 0
    y = 99
    location = [x, y]

   # X의 좌표를 찾는다
    for i in range(len(arr)):
            if arr[99][i] == 2:
                x = i

    while  y > 0:
        # 만약 왼쪽에 공간이 있고 왼쪽 값이 1이라면 왼쪽 좌표로 업데이트
        if x > 0 and arr[y][x-1] == 1:
            while x > 0 and arr[y][x-1] == 1:
                x -= 1

        # 만약 오른쪽에 공간이 있고 오른쪽 값이 1이라면 오른쪽 좌표로 업데이트
        elif x < 99 and arr[y][x+1] == 1:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
        # 더 이상 좌우로 갈 수 없다면 위로 올라가기
        y -= 1

    print(f'#{tc} {x}')







    # p_location = []
    # l_location =[]
    # r_location = []
    #
    # for i in range(99, -1, -1):
    #     for j in range(99, -1, -1):
    #         if arr[i][j] == 2:
    #             p_location = [i-1, j]
    #
    #         # 위로 올라가는 경우
    #         if i == p_location[0] and j == p_location[1]:
    #             if arr[i][j-1] == 0 and arr[i][j+1] ==0 and arr[i-1][j] == 1:
    #                 p_location = [i-1, j]
    #             elif arr[i][j-1] == 1:
    #                 l_location = [i, j-1]
    #             elif arr[i][j+1] == 1:
    #                 r_location = [i, j+1]
    #
    #         # 왼쪽으로 가는 경우
    #         if i == l_location[0] and j == l_location[1]:
    #             if arr[i][j-1] == 1:
    #                 l_location = [i, j-1]
    #
    #         # 오른쪽으로 가는 경우
    #             elif i == r_location[0] and j == r_location[1]:
    #                 if arr[i][j+1] == 1:
    #                     r_location = [i, j+1]









