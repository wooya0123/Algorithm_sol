import sys
sys.stdin = open('input.txt')




T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    test_col = []
    test_box = []
    result = 1

    # 가로, 세로 검증
    for i in range(9):
        if len(set(puzzle[i])) != 9:
            result = 0
            break
        for j in range(9):
            test_col.append(puzzle[j][i])
        if len(set(test_col)) != 9:
            result = 0
        else:
            test_col = []

        if result == 0:
            break

    # 격자 검증
    if result != 0:
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):        # 조사할 꼭짓점 x, y
                for m in range(3):
                    for n in range(3):
                        test_box.append(puzzle[x+m][y+n])

                if len(set(test_box)) != 9:
                    result = 0
                else:
                    test_box = []

    print(f'#{tc} {result}')