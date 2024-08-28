import sys
sys.stdin = open('input.txt')

def in_order(T):
    exp = []
    if T:
        exp += in_order(left[T])
        exp += [node[T]]
        exp += in_order((right[T]))

        if len(exp) == 3:                   # 리스트에 숫자-연산자-숫자가 됐을 때 연산하고 반환
            if exp[1] == '+':
                exp = [exp[0] + exp[2]]

            elif exp[1] == '-':
                exp = [exp[0] - exp[2]]

            elif exp[1] == '*':
                exp = [exp[0] * exp[2]]

            else:
                exp = [exp[0] / exp[2]]
    return exp

T = 10

for tc in range(1, 11):
    N = int(input())

    node = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            n, o, l, r = data
            n, l, r = int(n), int(l), int(r)
            node[n] = o
            left[n] = l
            right[n] = r
        else:
            n, num = data
            n, num = int(n), int(num)
            node[n] = num

    result = in_order(1)
    print(f'#{tc}',int(*result))