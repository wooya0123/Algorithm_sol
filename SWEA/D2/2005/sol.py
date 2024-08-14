import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(n):
    if n == 1:
        return [1]
    else:
        return [1] + [pascal(n-1)[i] + pascal(n-1)[i+1] for i in range(len(pascal(n-1)) - 1)] + [1]

def print_pascal(n):
    for j in range(1, n+1):
        result = pascal(j)
        print(*result)


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    print_pascal(N)



# def pascal(lst, n, end):
#     if n == end:
#         return lst
#     else:
#         lst = [1] + [pascal(end - 1)[i] + pascal(end - 1)[i + 1] for i in range(len(pascal(end - 1)) - 1)] + [1]
#         lst += lst + [pascal(lst, n+1, end)]
# result = pascal([0], 0, 5)
# print(result)

