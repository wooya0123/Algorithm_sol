import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]     # 1: N극 2: S극
    visited = [[0] * N for _ in range(N)]       # 탐색한 자석인지 판단

    # 세로로 탐색하면서 1->2 순서면 1개 카운트

    # 배열에서 1이 나오면 아래 쪽 탐색 1이 나오면 중단, 2가 나오면 카운트 1

    cnt = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:      # 탐색한 곳이 1이면
                n = 1
                while x+n < 100:    # 아래로 계속 내려가면서 2가 나오는지 찾기
                    if arr[x+n][y] == 2:    # 2가 나오면 break
                        if visited[x+n][y] == 0:    # 한 번도 교착상태로 판단하지 않은 자석이면 갯수 세기
                            cnt += 1
                            visited[x + n][y] = 1   # 탐색했다고 표시
                        break
                    n += 1
    print(f'#{tc} {cnt}')




    # move = 0
    # # 1은 아래로, 2는 위로
    # while move > 0:
    #     for i in range(99):
    #         for j in range(100):
    #             if arr[i+1][j] == 0:    # 움직일 곳이 비어있다면
    #                 if arr[i][j] == 1:  # 1은 아래로
    #                     arr[i][j] = 0
    #                     arr[i+1][j] = 1
    #
    #             if arr[i-1][j] == 0:    # 움직일 곳이 비어 있다면
    #                 if arr[i][j] == 2:  # 2는 위로
    #                     arr[i][j] = 0
    #                     arr[i-1][j] = 2