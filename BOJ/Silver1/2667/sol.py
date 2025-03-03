N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
res = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            stack = [(i,j)]
            arr[i][j] = 0
            cnt = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                        stack.append((nx, ny))
                        arr[nx][ny] = 0
                        cnt += 1
            res.append(cnt)
print(len(res))
for r in sorted(res):
    print(r)