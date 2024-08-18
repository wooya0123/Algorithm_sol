import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    stack = []

    result = 0
    i = -1

    # 문자열 끝까지 순회
    while i <= len(numbers) - 2:
        i += 1
        if numbers[i] == '1':   # 1이면 스택에 넣기
            stack += [numbers[i]]
        elif numbers[i] == '0': # 0이면 스택 다 꺼내서 개수 세기
            cnt_one = 0
            while stack:
                stack.pop()
                cnt_one += 1
            if result < cnt_one:
                result = cnt_one
    cnt_one = 0
    while stack:        # 마지막이 1로 끝났을 때 스택 다 꺼내서 개수 세기기
       stack.pop()
       cnt_one += 1
    if result < cnt_one:
        result = cnt_one

    print(f'#{tc} {result}')