R, C = list(map(int, input().split()))
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

current = (0, 0)
way = set(arr[0][0])
visited[0][0] = 1
res = 1

def dfs(current, way, visited, move):
    global res

    x, y = current
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and arr[nx][ny] not in way:
            visited[nx][ny] = 1
            way.add(arr[nx][ny])
            dfs((nx, ny), way, visited, move+1)
            visited[nx][ny] = 0
            way.remove(arr[nx][ny])
    else:
        if res < move:
            res = move
            return

dfs(current, way, visited, 1)
print(res)