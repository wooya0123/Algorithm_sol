from collections import deque

def solution(board):
    row = len(board)        # 행
    col = len(board[0])     # 열
    visited = [[0] * col for _ in range(row)]

    q = deque()
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                q.append((i, j, 0))     # 시작지점 덱에 추가
                visited[i][j] = 1       # 시작지점 방문 표시
                break

    min_turn = 1e9
    while q:
        x, y, turn = q.popleft()        # 행, 열, 움직인 횟수
        if board[x][y] == 'G':          # 도착 지점이면 움직인 횟수 중 최소 값을 찾기
            if min_turn > turn:
                min_turn = turn
        
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != 'D':    # 움직일 수 있는 점인지 확인
                # 움직일 수 있는 곳까지 움직이기
                while True:
                    nx += dx
                    ny += dy
                    if 0 <= nx < row and 0 <= ny < col:             # 보드를 벗어나지 않고
                        if board[nx][ny] == '.':                    # 움직일 수 있는 점이면 다시 움직이기
                            continue
                        elif board[nx][ny] == 'D':                  # 막힌 곳이면 이전 점을 저장, 방문표시
                            if visited[nx-dx][ny-dy] == 0:
                                q.append((nx-dx, ny-dy, turn+1))
                                visited[nx-dx][ny-dy] = 1
                                break
                            else:
                                break
                    else:                                           # 보드를 벗어났다면 이전 점을 저장, 방문표시
                        if visited[nx - dx][ny - dy] == 0:
                            q.append((nx - dx, ny - dy, turn + 1))
                            visited[nx - dx][ny - dy] = 1
                            break
                        else:
                            break

    if min_turn == 1e9:
        min_turn = -1
    return min_turn

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))