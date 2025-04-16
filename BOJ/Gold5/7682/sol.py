while True:
    arr = input()
    if arr == 'end':
        break

    X_cnt = arr.count('X')
    O_cnt = arr.count('O')
    dot_cnt = arr.count('.')

    # X와 O의 개수 유효성 검사
    if O_cnt > X_cnt or X_cnt > O_cnt + 1:
        print('invalid')
        continue
    if dot_cnt == 9:
        print('invalid')
        continue

    res = {'X': 0, 'O': 0}
    row_board = [list(arr[:3]), list(arr[3:6]), list(arr[6:])]
    col_board = list(zip(row_board[0], row_board[1], row_board[2]))
    ans = 'invalid'

    # 가로 세로
    for i in range(3):
        if row_board[i][0] == row_board[i][1] == row_board[i][2]:
            if row_board[i][0] == 'O':
                res['O'] += 1
            elif row_board[i][0] == 'X':
                res['X'] += 1

        if col_board[i][0] == col_board[i][1] == col_board[i][2]:
            if col_board[i][0] == 'O':
                res['O'] += 1
            elif col_board[i][0] == 'X':
                res['X'] += 1

    # 대각선
    if row_board[0][0] == row_board[1][1] == row_board[2][2] and row_board[0][0] != '.':
        if row_board[0][0] == 'X':
            res['X'] += 1
        elif row_board[0][0] == 'O':
            res['O'] += 1
    elif row_board[0][2] == row_board[1][1] == row_board[2][0] and row_board[0][2] != '.':
        if row_board[0][2] == 'X':
            res['X'] += 1
        elif row_board[0][2] == 'O':
            res['O'] += 1

    if res['X'] > 0 and res['O'] == 0 and X_cnt == O_cnt + 1:
        ans = 'valid'
    elif res['O'] > 0 and res['X'] == 0 and X_cnt == O_cnt:
        ans = 'valid'
    elif res['X'] == 0 and res['O'] == 0 and dot_cnt == 0 and X_cnt == 5 and O_cnt == 4:
        ans = 'valid'
    print(ans)