import sys
sys.stdin = open('input.txt')

def calculator(expression):
    # 연산자의 우선 순위를 dict 형태로 구현
    op = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
    }
    result = ''
    stack = []

    for exp in expression:
        if exp.isdigit():   # 숫자면 바로 출력
            result += exp
        elif exp == '(':    # 여는 괄호면 스택에 넣기
            stack.append(exp)
        elif exp == ')':    # 닫는 괄호면 스택에서 여는 괄호 나올 때까지 빼서 출력
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()     # 여는 괄호도 스택에서 빼주기
        elif exp in op:     # 연산자라면 스택 안에 있는 연산자가 우선순위가 낮은 게 나올 때까지 빼서 출력
            while stack and op[exp] <= op[stack[-1]]:
                result += stack.pop()
            stack.append(exp)   # 다 뺐으면 자신을 스택에 넣기
    while stack:    # 연산 끝났으면 스택이 빌 때까지 결과 출력
        result += stack.pop()
    return result

def calcuation(expression):
    stack = []
    for exp in expression:
        if exp.isdigit():
            stack.append(int(exp))  # 숫자라면 int로 변환해서 스택에 넣기
        else:
            n2 = stack.pop()        # 연산자라면 스택에서 숫자 빼와서 연산
            n1 = stack.pop()
            if exp == '+':
                result = n1 + n2
            elif exp == '-':
                result = n1 - n2
            elif exp == '*':
                result = n1 * n2
            else:
                result = n1 / n2

            stack.append(result)    # 연산한 결과를 스택에 넣기
    return stack[-1]                # 마지막 결과 출력

T = 10

for tc in range(1, 11):
    N = int(input())
    expression = input()

    result = calculator(expression)
    answer = calcuation(result)
    print(f'#{tc} {answer}')