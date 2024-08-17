import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(str, input()))
    new_arr = []

    # 레이저를 0으로 표시한 new_arr
    for k in range(len(arr)):
        if arr[k] == '(' and arr[k+1] == ')':
            new_arr += [0]
        elif arr[k] == ')' and arr[k-1] == '(':
            continue
        else:
            new_arr += arr[k]


    # 레이저가 막대기를 자르면 개수가 1개가 더 늘어남
    stack = []
    result = 0

    # 스택에 ( 는 집어넣고 )가 나오면 pop, 레이저가 나오면 스택에 들어있는 수만큼 막대기 개수 추가
    for x in new_arr:
        if x == '(':
            stack += [x]
            result += 1
        elif x == ')':
            stack.pop()
        else:
            result += len(stack)
    print(f'#{tc} {result}')

