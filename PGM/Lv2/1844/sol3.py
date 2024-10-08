from collections import deque
def solution(maps):
    n = len(maps)       # 행
    m = len(maps[0])    # 열
    start = (0,0)       # 출발 지점
    goal = (n-1, m-1)   # 도착 지점

    Q = deque()
    Q.append(start)
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    visited[n-1][m-1] = 1e9

    while Q:
        x, y = Q.pop()

        for dx, dy in [1,0], [0,1], [-1,0], [0,-1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] <= visited[n-1][m-1]:
                # 한 번도 방문 안 한 곳이면
                if visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                # 방문한 적이 있는 곳이면 -> 값을 비교해서 작은 값을 저장
                else:
                    temp = visited[x][y] + 1
                    if visited[nx][ny] < temp:
                        continue
                    else:
                        visited[nx][ny] = temp
                        Q.append((nx, ny))


    if visited[n-1][m-1] == 1e9:
        return -1
    else:
        return visited[n-1][m-1]