from collections import deque

def solution(land):
    row = len(land)         # 행
    col = len(land[0])      # 열

    oil = {}                # 석유 블럭을 그룹별로 묶어서 딕셔너리에 담기
    group = 11              # 각 그룹 구분용
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1:         # 한 번도 시추하지 않은 석유 블럭이면 bfs로 그룹 짓기
                q = deque()
                q.append((i, j))
                land[i][j] = group      # 시추했다고 표시
                cnt = 1                 # 석유 블럭 개수 세기

                while q:
                    x, y = q.popleft()

                    for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < row and 0 <= ny < col and land[nx][ny] == 1:
                            q.append((nx, ny))
                            cnt += 1
                            land[nx][ny] = group    # 시추한 곳은 group으로 바꿔둠

                oil[group] = cnt        # oil 딕셔너리에 group을 키값으로 석유 덩어리 수 저장
                group += 1              # 다음 group 탐색


    max_oil = -1
    for j in range(col):        # 열 순회
        i = 0                   # 행 증가용
        oil_tank = set()
        oil_cnt = 0
        while i < row:          # 시추하면서 석유 블럭 그룹을 set에 넣기
            if land[i][j] != 0:
                oil_tank.add(land[i][j])
            i += 1

        for o in oil_tank:      # oil 딕셔너리에서 석유 블럭 개수 가져오기
            oil_cnt += oil[o]

        if max_oil < oil_cnt:   # 최댓값 갱신
            max_oil = oil_cnt

    return max_oil

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

print(solution(land))