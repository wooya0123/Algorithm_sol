import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    start = []          # 돌이 있는 곳만 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                start += [[i, j]]

    result = 0
    for current_x, current_y in start:      # 돌이 있는 좌표를 현재 위치로 설정
        for dx, dy in [-1,0], [1,0], [0,-1], [0,1], [-1,1], [1,1], [1,-1], [-1,-1]:     # 상하좌우 우상 우하 좌하 좌상
            nx = current_x + dx
            ny = current_y + dy

            cnt = 0
            # 탐색하면서 다음 위치가 돌이 있는 경우만 반복
            while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                cnt += 1    # 돌이 있으면 cnt 증가
                nx += dx    # 다음 위치로 이동
                ny += dy

            if cnt >= 4:    # 오목이 됐으면 결과 출력, result 증가 후 반복 중단
                print(f'#{tc} YES')
                result += 1
                break

        if result > 0:  # 현재 위치를 바꾸기 전 오목이 됐는지 체크 후 중단
            break
    if result == 0:     # 반복문을 다 돌았는데 결과가 0이면 결과 출력
        print(f'#{tc} NO')