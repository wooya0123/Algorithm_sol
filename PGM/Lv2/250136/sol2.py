# 석유 시추한 곳은 -1로 바꾸고 시추관이 내려가서 -1에 닿으면 시추한 곳만큼 그냥 더하기(다시 탐색 X)

from collections import deque

def solution(land):
    row = len(land)         # 행
    col = len(land[0])      # 열

    oil = [[0, 0] * (col+1)]     # 열마다 시추한 석유 기록(idx: 열 번호, 값: 시추한 석유 덩어리 수)
    max_cnt = -1
    for j in range(col):    # 열 순회
        i = 0               # 행 증가용
        cnt = 0             # 시추한 석유 덩어리 수
        while i < row:
            if land[i][j] == 0:             # 해당 칸이 땅일 때
                i += 1
                continue
            elif land[i][j] != 1:           # 해당 칸이 이미 시추한 곳일 때
                if oil[j+1][1] == -1:
                    cnt += oil[land[i][j] // 10][0]         # 바로 석유 수 더해주기
                    oil[j+1][1] = land[i][j] // 10          # 참고한 열 기록

            elif land[i][j] == 1:
                land[i][j] = (j+1) * 10    # 해당 칸 석유 시추
                cnt += 1

                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for dx, dy in [-1,0], [1,0], [0,-1], [0,1]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < row and 0 <= ny < col and land[nx][ny] == 1:
                            q.append((nx, ny))
                            land[nx][ny] = (j+1) * 10    # 해당 열에서는 시추했다고 표시
                            cnt += 1
                oil[j+1][0] = cnt
                i += 1

        if max_cnt < cnt:
            max_cnt = cnt


    return max_cnt

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land))