import sys
sys.stdin = open('sample_input.txt')

def cal(num1, num2, op_idx):
    if op_idx == 0:
        return num1 + num2
    elif op_idx == 1:
        return num1 - num2
    elif op_idx == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(abs(num1) // num2)
        else:
            return num1 // num2



def dfs(lev, total):
    global max_num, min_num

    if lev == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    for i in range(4):
        if op[i] == 0:
            continue

        op[i] -= 1
        dfs(lev+1, cal(total, num[lev], i))
        op[i] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 숫자 개수
    op = list(map(int, input().split()))     # 각 연산자 개수
    num = list(map(int, input().split()))   # 숫자들
    max_num = -1e9
    min_num = 1e9

    dfs(1, num[0])

    print(f'#{tc} {max_num - min_num}')
