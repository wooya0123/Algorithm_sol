import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())                                            # 격자판 크기
    arr = [input() for _ in range(N)]                           # 배열
    visited = [[0] * N for _ in range(N)]                       # 방문 처리
    progress = 0        # 1이면 사각형인지 보는 중
    side = 0
    r_cnt = 0           # 세로 길이

    for i in range(N):
        c_cnt = 0       # 가로 길이
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] == '#':     # 방문한 적 없고 #이면
                visited[i][j] = 1                           # 방문 처리하고
                c_cnt += 1                                  # 해당 부분부터 사각형인지 확인
                r_cnt += 1
                while j < N-1:                              # 열 순회 -> 방문처리, 가로 길이 체크
                    j += 1
                    if arr[i][j] == '#':
                        visited[i][j] = 1
                        c_cnt += 1
                    else:
                        break
                if progress == 0 and side < c_cnt:           # 첫 사각형 탐색할 때 변의 길이를 저장하고 사각형 보는 중이라고 기록
                    side = c_cnt
                    progress = 1
                elif progress == 1 and side != c_cnt:        # 사각형 보는 중인데 가로 길이가 변의 길이랑 다르면 break
                    progress = -1
                    break
        if progress == -1:
            break
    if progress == 1 and side == r_cnt:             # 큰 사각형이라고 했을 때 변의 길이 = 가로 길이 = 세로 길이여야 함
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')