import sys
sys.stdin = open('sum_input.txt')

T = 10

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    cross = 0
    r_cross = 0
    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                cross += arr[i][j]
            if (99 - i) == j:
                r_cross += arr[i][j]
        if result < row:
            result = row
        if result < col:
            result = col
    if result < cross:
        result = cross
    if result < r_cross:
        result = r_cross

    print(f'#{tc} {result}')