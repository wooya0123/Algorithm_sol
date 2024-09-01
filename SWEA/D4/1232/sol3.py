import sys
sys.stdin = open('input.txt')

def in_order(T):
    value = node[T][0]
    left = node[T][1]
    right = node[T][2]

    if T:
        if value.isdigit():
            return int(value)
        else:
            num1 = in_order(left)
            num2 = in_order(right)
            if value == '+':
                answer = num1 + num2

            elif value == '-':
                answer = num1 - num2

            elif value == '*':
                answer = num1 * num2

            else:
                answer = num1 / num2

            return answer
T = 10

for tc in range(1, 11):
    N = int(input())
    node = [[0, 0, 0] for _ in range(N+1)]  # idx: 노드 번호, 값/왼/오

    for _ in range(N):
        data = input().split()

        if len(data) == 4:
            n, v, l, r = data
            n, l, r = int(n), int(l), int(r)
            node[n][0] = v
            node[n][1] = l
            node[n][2] = r
        else:
            n, v = data
            n = int(n)
            node[n][0] = v

    root = 1
    res = in_order(root)
    print(f'#{tc} {res:.0f}')
