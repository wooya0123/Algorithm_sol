# def comb(lev, start):
#     if lev == N//2:
#         A.append(path[:])
#         return
#
#     for i in range(start, N):
#         if visited[i] == 1:
#             continue
#         else:
#             path.append(ing_lst[i])
#             visited[i] = 1
#             comb(lev+1, start+1)
#             path.pop()
#             visited[i] = 0

# def make_A(arr, lev, start):
#     if lev == 2:
#         food_A.append(path2[:])
#         return

#     for i in range(start, len(arr)):
#         if visited2[i] == 1:
#             continue
#         else:
#             path2.append(arr[i])
#             visited2[i] = 1
#             make_A(arr, lev+1, start+1)
#             path2.pop()
#             visited2[i] = 1


# def make_B(arr, lev, start):
#     if lev == 2:
#         food_B.append(path2[:])
#         return

#     for i in range(start, len(arr)):
#         if visited2[i] == 1:
#             continue
#         else:
#             path2.append(arr[i])
#             visited2[i] = 1
#             make_B(arr, lev + 1, start + 1)
#             path2.pop()
#             visited2[i] = 1


# def perm_A(arr, cnt, n):
#     if cnt == n:
#         food_A.append((ingredient[path2[0]][path2[1]]))
#         return
#     for i, val in enumerate(arr):
#         if visited_A[i] == 1:
#             continue
#         else:
#             path2.append(val)
#             visited_A[i] = 1
#             perm_A(arr, cnt+1, n)
#             path2.pop()
#             visited_A[i] = 0
#
# def perm_B(arr, cnt, n):
#     if cnt == n:
#         food_B.append((ingredient[path2[0]][path2[1]]))
#         return
#     for i, val in enumerate(arr):
#         if visited_B[i] == 1:
#             continue
#         else:
#             path2.append(val)
#             visited_B[i] = 1
#             perm_B(arr, cnt+1, n)
#             path2.pop()
#             visited_B[i] = 0

import sys
sys.stdin = open('sample_input.txt')

def subset(ing_lst):
    path = []
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                path.append(ing_lst[j])
        if len(path) == N//2:
            A.append([*path])
            path = []
        else:
            path = []

def subset(start, path):
    if len(path) == N//2:
        A.append(path)
        return

    for i in range(start, N):
        subset(i+1, path+[ing_lst[i]])

def food(a):
    global res
    b = list(set(ing_lst) - set(a))
    food_A = 0
    food_B = 0
    for i in range(N//2):
        for j in range(N//2):
            food_A += ingredient[a[i]][a[j]]
            food_B += ingredient[b[i]][b[j]]
    ans = abs(food_A - food_B)
    if res > ans:
        res = ans
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 식재료의 수
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    ing_lst = list(range(N))
    res = 99999

    # 식재료를 2그룹으로 나누기(조합)
    A = []
    # B = []

    visited = [0] * N
    # subset(ing_lst)
    subset(0, [])
    # for a in A:
    #     B.append(list(set(ing_lst) - set(a)))

    # 각 그룹의 식재료들의 조화를 모두 더하기
    for a in A:
        food(a)
    print(f'#{tc} {res}')













    # # 나눈 그룹에서 순서 고려해서 뽑기(순열)
    # food_B = []
    # visited2 = [0] * (N//2)
    # path2 = []

    # for x in A:
    #     food_A = []
    #     food_B = []

    #     make_A([x[0], x[1]], 0, 0)
    #     make_B(x[2], 0, 0)

    #     for q in food_A:
    #         temp = ingredient[q[0]][q[1]]
    #         for r in food_B:
    #             ans = temp - ingredient[r[0]][r[1]]
    #             if res > ans:
    #                 res = ans
    # print(res)

    # for a in A:
    #     perm_A(a, 0, 2)
    # for b in B:
    #     perm_B(b, 0, 2)
    #
    # for k in range(len(food_A)):
    #     ans = abs(food_A[k] - food_B[k])
    #     if res > ans:
    #         res = ans




