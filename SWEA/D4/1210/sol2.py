import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]

    stack = []
    for k in range(100):
        if arr[99][k] == 2:
            stack.append([99, k])

    result = None
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for dx, dy in [-1,0], [0,-1], [0,1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] != 0 and visited[nx][ny] != 1:
                stack.append([nx, ny])

        if x == 0 and arr[x][y] == 1:
            result = y
            break

    print(f'#{tc} {result}')