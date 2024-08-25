import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]

    result = []

    for i in range(N):
        if N > M:
            for j in range(0, N-M):
                for k in range(M//2):
                    # 가로 탐색
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        result = []
                        break
                    else:
                        result += [[i, j]]

                    # 세로 탐색
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        result = []
                        break
                    else:
                        result += [[i, j]]
                if result:
                    break
            if result:
                break
        else:
            for k in range(M // 2):
                # 가로 탐색
                if arr[i][k] != arr[i][N-1-k]:
                    result = []
                    break
                else:
                    result += [[i, k]]

                # 세로 탐색
                if arr[k][i] != arr[N-1-k][i]:
                    result = []
                    break
                else:
                    result += [[i, k]]
            if result:
                break
    print(result)



    # # 가로 조사
    # for i in range(N):
    #     row_text = arr[i]
    #     row_length = len(row_text)
    #     if row_length % 2 == 0:
    #         row_rep = int(row_length // 2)
    #     else:
    #         row_rep = int((row_length - 1) // 2)
    #
    #
    #     for k in range(row_rep):
    #         if row_text[k] != row_text[N-1-k]:
    #             break
    #         print(''.join(row_text))
    #         break
    #
    # # 세로 조사
    # for i in range(N):
    #     col_text = []
    #     for j in range(M):
    #         col_text += arr[j][i]
    #     col_length = len(col_text)
    #     if col_length % 2 == 0:
    #         col_rep = int(col_length // 2)
    #     else:
    #         col_rep = int((col_length - 1) // 2)
    #
    #     for m in range(col_rep // 2):
    #         if col_text[m] != col_text[N-1-m]:
    #             break
    #         print(''.join(col_text))
    #         break





# for i in range(N):
    #     text = input()
    #     split_text = list(text)
    #     reversed_text = text[::-1]
    #
    #     even_pattern = int(len(split_text) / 2)
    #     odd_pattern = int((len(split_text) - 1) / 2)
    #
    #     if M % 2 == 0:
    #         pattern = text[0:even_pattern]
    #         target = reversed_text[0:even_pattern]
    #     else:
    #         pattern = text[0:odd_pattern]
    #         target = reversed_text[0:odd_pattern]
    #
    #     if pattern == target:
    #         print(text)