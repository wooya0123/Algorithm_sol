import sys
sys.stdin = open('s_input.txt')

T = int(input())


def check_num(str_num):
    # 끝까지 비교해야하므로 False인 경우 바로 False 반환하고 True인 경우 계속 반복문 진행하게끔
    for i in range(len(str_num) - 1):
        if int(str_num[i]) > int(str_num[i + 1]):
            return False
    return True

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num_lst = []
    result = -1     # 단조인 수가 없을 경우 -1 반환

    for i in range(len(num) -1):
        for j in range(i+1, len(num)):
            mul_num = num[i] * num[j]
            if check_num(str(mul_num)):
                if result < mul_num:
                    result = mul_num

    print(f'#{tc} {result}')