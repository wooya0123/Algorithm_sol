import sys
sys.stdin = open('sum_input.txt')

for _ in range(1, 11):
    tc = int(input())

    # 2차원 배열 받아오기
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합의 최대값 미리 설정
    max_sum = 0

    # 단축 버전
    sum_rd = 0
    sum_ld = 0
    for i in range(100):
        sum_r = 0
        sum_c = 0
        for j in range(100):
            sum_r += arr[i][j]
            sum_c += arr[j][i]
            if i == j:
                sum_rd += arr[i][j]
            if (100 - 1) - i == j:
                sum_ld += arr[i][j]
        if sum_r >= max_sum:
            max_sum = sum_r
        if sum_c >= max_sum:
            max_sum = sum_c
    if sum_rd >= max_sum:
        max_sum = sum_rd
    if sum_ld >= max_sum:
        max_sum = sum_ld

    print(f'#{tc} {max_sum}')
    
    # # 풀어서 쓴 버전
    # # 각 행의 합을 구해서 max_sum 보다 크면 max_sum에 할당
    # for i in range(100):
    #     sum_r = 0
    #     for j in range(100):
    #         sum_r += arr[i][j]
    #     if sum_r >= max_sum:
    #         max_sum = sum_r
    #
    # # 각 열의 합을 구해서 max_sum 보다 크면 max_sum에 할당
    # for j in range(100):
    #     sum_c = 0
    #     for i in range(100):
    #         sum_c += arr[i][j]
    #     if sum_c >= max_sum:
    #         max_sum = sum_c
    #
    # # 왼 -> 오 대각선의 합을 구해서 max_sum 보다 크면 max_sum에 할당
    # sum_rd = 0
    # for i in range(100):
    #     for j in range(100):
    #         if i == j:
    #             sum_rd += arr[i][j]
    #     if sum_rd >= max_sum:
    #         max_sum = sum_rd
    #
    # # 오 -> 왼 대각선 합을 구해서 max_sum 보다 크면 max_sum에 할당
    # sum_ld = 0
    # for i in range(100):
    #     for j in range(100):
    #         if (100 - 1) - i == j:
    #             sum_ld += arr[i][j]
    #     if sum_ld >= max_sum:
    #         max_sum = sum_ld
    #
    # print(f'#{tc} {max_sum}')







