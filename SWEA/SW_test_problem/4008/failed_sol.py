import sys
sys.stdin = open('sample_input.txt')

def perm(lev, path):
    # 기저 조건
    if lev == len(op):
        op_lst.append([*path])
        return

    for i, val in enumerate(op):
        if visited[i] == 1:
            continue
        else:
            path.append(val)
            visited[i] = 1
            perm(lev+1, path)
            path.pop()
            visited[i] = 0
    pass

def calculation(arr):
    result = arr[0]
    for i in range(1, len(arr), 2):
        operator = arr[i]
        num = arr[i+1] if i < len(arr) - 1 else 0

        if operator == '+':
            result = result + num
        elif operator == '-':
            result = result - num
        elif operator == '*':
            result = result * num
        elif operator == '/':
            if result < 0:
                result = -(abs(result) // num)
            else:
                result = result // num

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 숫자 개수
    plus, minus, multiple, divide = list(map(int, input().split()))     # 각 연산자 개수
    num = list(map(int, input().split()))   # 숫자들
    op = ['+'] * plus + ['-'] * minus + ['*'] * multiple + ['/'] * divide    # 연산자들
    max_res = -1e9
    min_res = 1e9
    res_lst = set()

    # 연산자를 순열로 가능한 경우 모두 구하기
    op_lst = []
    visited = [0] * len(op)
    perm(0, [])

    # for문으로 숫자 사이에 넣어 배열 생성
    arr = [0] * (N + N)
    for o in op_lst:
        for i in range(N):
            arr[2*i] = num[i]
            arr[2*i+1] = o[i] if i < N-1 else '='
        res = calculation(arr)
        res_lst.add(res)

    print(max(res_lst) - min(res_lst))



