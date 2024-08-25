import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for j in range(100):
        if arr[0][j] == 1:
            start.append([0,j])

    max_cnt = 0
    X = 0
    for x, y in start:
        visited = [[0] * 100 for _ in range(100)]
        visited[x][y] = 1
        cnt = 0
        while x < 99:
            # 왼쪽에 1이 있는지
            while 0 <= y:
                if arr[x][y-1] == 1 and visited[x][y-1] == 0:
                    y = y-1
                    cnt += 1
                    visited[x][y] = 1
                else:
                    break
            # 오른쪽에 1이 있는지
            while y < 99:
                if arr[x][y+1] == 1 and visited[x][y+1] == 0:
                    y = y+1
                    cnt += 1
                    visited[x][y] = 1
                else:
                    break
            # 왼, 오에 1이 없으면 내려가기
            if x < 98 and arr[x+1][y] != 0:
                x += 1
                cnt += 1
                visited[x][y] = 1
            else:
                break

        if x == 99 and max_cnt <= cnt:
            max_cnt = cnt
            X = y
    print(max_cnt, X)

    