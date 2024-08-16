import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    play_data = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]

    board[N // 2][N // 2 - 1] = board[N // 2 - 1][N // 2] = 1   # 흑돌 초기 세팅
    board[N//2][N//2] = board[N//2 - 1][N//2 - 1] = 2   # 백돌 초기 세팅

    for play in play_data:
        x = play[0] - 1
        y = play[1] - 1
        # 흑, 백돌 놓기
        if play[-1] == 1:
            board[x][y] = 1
        else:
            board[x][y] = 2


        # 델타 탐색으로 자신의 돌 사이에 상대 돌이 있으면 내 돌로 바꾸기
        for dx, dy in [-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]:    # 상하좌우 우상 우하 좌하 좌상
            nx = x + dx  # 주위에 상대 돌이 있는지 파악
            ny = y + dy
            b_stack = []  # 흑돌로 바꿀 백돌
            w_stack = []  # 백돌로 바꿀 흑돌
            while 0 <= nx < N and 0 <= ny < N and play[-1] == 1 and board[nx][ny] == 2:              # 흑돌 턴인 경우
                b_stack += [[nx, ny]]     # 해당 돌을 스택에 넣어둠
                nx += dx
                ny += dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:    # 끝에 흑돌이 나왔다면 스택에 있는 모든 돌을 흑돌으로
                for change in b_stack:
                    cx = change[0]
                    cy = change[1]
                    board[cx][cy] = 1
            while 0 <= nx < N and 0 <= ny < N and play[-1] == 2 and board[nx][ny] == 1:
                    w_stack += [[nx, ny]]     # 해당 돌을 스택에 넣어둠
                    nx += dx
                    ny += dy

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 2:    # 끝에 백돌이 나왔다면 스택에 있는 모든 돌을 백돌으로
                for change in w_stack:
                    cx = change[0]
                    cy = change[1]
                    board[cx][cy] = 2

    b_cnt = 0
    w_cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1
    print(f'#{tc} {b_cnt} {w_cnt}')

    