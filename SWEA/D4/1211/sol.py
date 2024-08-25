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

    distance = 9999
    result = 0
    stack = []
    for x,y in start:
        visited = [[0] * 100 for _ in range(100)]
        stack = [[x,y]]
        visited[x][y] = 1
        while stack:
            x, y = stack.pop()
            if x == 99:
                if distance > visited[x][y] - 1:
                    distance = visited[x][y] - 1
                    result = y
                elif distance == visited[x][y] - 1 and result < y:
                    result = y

            for dx, dy in [0,-1], [0,1], [1,0]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] != 0 and visited[nx][ny] == 0:
                    stack.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    print(result)

    