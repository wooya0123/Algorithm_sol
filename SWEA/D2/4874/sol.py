import sys
sys.stdin = open('sample_input.txt')


def forth(expression):
    stack = []
    op = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    cnt_op = 0
    cnt_num = 0

    for exp in expression:
        if exp in op:
            cnt_op += 1
        else:
            cnt_num += 1

        if cnt_op >= cnt_num:   # 연산자가 숫자보다 많으면 연산 불가
            return 'error'
        elif cnt_op == 0 and cnt_num == len(expression):    # 연산자 없이 숫자만 있는 경우
            return 'error'


        if exp.isdigit():       # 숫자면 stack에 int 형태로 넣기
            stack.append(int(exp))
        elif exp == '.':    # .이면 반복문 중단
            break
        elif exp in op and len(stack) >= 2:     # 스택에 숫자 2개 이상이고 연산자면 계산
            n2 = stack.pop()
            n1 = stack.pop()
            if exp == '+':
                result = n1 + n2
            elif exp == '-':
                result = n1 - n2
            elif exp == '*':
                result = n1 * n2
            else:
                result = n1 // n2
            stack.append(result)

    if len(stack) == 1:     # 스택 안에 요소가 1개만 있을 경우 출력
        return stack[0]
    else:
        return 'error'

T = int(input())

for tc in range(1, T+1):
    expression = list(map(str, input().split()))

    result = forth(expression)
    print(f'#{tc} {result}')