R, C = input().split()
R, C = int(R), int(C)
arr = [list(input()) for _ in range(R)]
way = set(arr[0][0])
res = 1

def dfs(x, y, way, move):
    global res
    res = max(res, move)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in way:
            way.add(arr[nx][ny])
            dfs(nx, ny, way, move + 1)
            way.remove(arr[nx][ny])
dfs(0, 0, way, 1)
print(res)