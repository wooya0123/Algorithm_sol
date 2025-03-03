N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
special_visit = [[0] * N for _ in range(N)]

normal = 0
special = 0

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            color = arr[i][j]

            if color == 'B':
                stack = [(i, j)]
                visit[i][j] = 1
                special_visit[i][j] = 1

                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0 and arr[nx][ny] == color:
                            stack.append((nx, ny))
                            visit[nx][ny] = 1
                            special_visit[nx][ny] = 1
                normal += 1
                special += 1

            else:
                stack = [(i, j)]
                visit[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0 and arr[nx][ny] == color:
                            stack.append((nx, ny))
                            visit[nx][ny] = 1
                normal += 1

                if special_visit[i][j] == 0:
                    stack = [(i, j)]
                    special_visit[i][j] = 1
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0<=nx<N and 0<=ny<N and special_visit[nx][ny] == 0:
                                if arr[nx][ny] == 'R' or arr[nx][ny] == 'G':
                                    stack.append((nx, ny))
                                    special_visit[nx][ny] = 1
                    special += 1

print(normal, special)
