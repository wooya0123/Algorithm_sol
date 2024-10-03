N, M = list(map(int, input().split()))  # N행 M열
r, c, d = list(map(int, input().split()))   # 현재 위치 r행 c열 d방향 보고 있음
arr = [list(map(int, input().split())) for _ in range(N)]

# 작동 시작 후 멈출 때까지 청소하는 칸의 개수
cnt = 0
cx = r
cy = c
direction = d
direction_order = [3, 2, 1, 0]

while 0 <= cx < N-1 and 0 <= cy < M-1 and arr[cx][cy] != 1:     # 움직인 곳이 방 안이고 벽이 아니라면
    if arr[cx][cy] == 0:    # 청소 안 한 곳이면 청소, 청소한 곳은 2로 표시
        cnt += 1
        arr[cx][cy] = 2
    else:
        # 델타 탐색 후 각 방향에 청소 안 한 곳은 좌표 넣고 그 외는 None 넣기
        stack = []
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:    # 북 동 남 서
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N-1 and 0 <= ny < M-1 and arr[nx][ny] == 0:
                stack.append((nx, ny))
            else:
                stack.append(None)

        # 청소기가 바라보는 방향에서 반시계 방향으로 돌면서 갈 곳이 있는지 판단 후 있으면 움직이기
        for _ in range(4):
            idx = 3 - direction
            direction = direction_order[(idx + 1) % 4]
            if stack[direction]:
                cx, cy = stack[direction]
                break
            else:
                continue
        # 청소기가 갈 곳이 없다면 후진(후진 했을 때 벽이라면 while문 조건에서 걸림)
        else:
            if direction == 0:
                cx += 1
            elif direction == 1:
                cy -= 1
            elif direction == 2:
                cx -= 1
            else:
                cy += 1
print(cnt)