# 석유 시추한 곳은 -1로 바꾸고 시추관이 내려가서 -1에 닿으면 시추한 곳만큼 그냥 더하기(다시 탐색 X)

from collections import deque

def solution(land):
    row = len(land)
    col = len(land[0])

    max_cnt = -1
    for j in range(col):
        n = j+1
        i = 0
        cnt = 0
        while i < row:
            if land[i][j] == n+1:
                i += 1
                continue
            if land[i][j] == 0:
                i += 1
                continue
            else:
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    if land[x][y] != 0 and land[x][y] <= n:
                        land[x][y] = n + 1
                        cnt += 1

                    for dx, dy in [-1,0], [1,0], [0,-1], [0,1]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < row and 0 <= ny < col and land[nx][ny] != 0 and land[nx][ny] <= n:
                            q.append((nx, ny))
                            land[nx][ny] = n + 1
                            cnt += 1
                i += 1
        if max_cnt < cnt:
            max_cnt = cnt


    return max_cnt

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land))