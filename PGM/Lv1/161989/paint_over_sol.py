def solution(n, m, section):
    wall = [1] * n   # 벽 구역 생성, 칠해야할 곳 0
    for paint in section:   # index == 구역 번호 - 1
        wall[paint-1] = 0

    cnt = 0
    for paint in section:
        current = paint-1
        if wall[current] == 0:
            for i in range(m):
                if current + i < n:
                    wall[current + i] = 1
                else:
                    break
            cnt += 1

    return cnt



n = 8
m = 4
section = [2, 3, 6]
result = 2
solution(n, m, section)