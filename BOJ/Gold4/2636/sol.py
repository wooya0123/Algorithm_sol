# 모두 녹는 데 걸리는 시간
# 모두 녹기 1시간 전 남아 있는 치즈 조각이 놓여 있는 칸 개수

from collections import deque

# 외부 공기 표시 함수
def check_outside_air():
    q = deque([(0, 0)])  # (0,0)에서 시작
    visited = [[False] * C for _ in range(R)]
    visited[0][0] = True

    while q:
        i, j = q.popleft()
        arr[i][j] = 2  # 외부 공기는 2로 표시

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                if arr[ni][nj] != 1:  # 치즈가 아닌 경우(빈 공간)만 큐에 추가
                    visited[ni][nj] = True
                    q.append((ni, nj))

# 1시간 뒤에 녹을 건지 판단 함수
def is_melt(i, j):
    res = False
    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 2:
            res = True
            break
    return res

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cheese_left = 1e9
time = -1

# 치즈가 하나도 안 남을 때까지 반복
while True:
    # 외부 공기 체크
    check_outside_air()

    time += 1   # 1시간 경과
    cheese = 0
    for i in range(R):
        for j in range(C):
            # 녹은 치즈 처리
            if arr[i][j] == -1:
                arr[i][j] = 0
            # 치즈 개수 세기
            if arr[i][j] == 1:
                cheese += 1
                # 1시간 뒤 녹을 치즈는 -1로 기록
                if is_melt(i, j):
                    arr[i][j] = -1

    # 다 녹기 1시간 전까지만 기록
    if cheese != 0:
        cheese_left = cheese
    else:
        break

print(time)
print(cheese_left)