import sys
sys.stdin = open('input.txt')

def in_order(T):
    ex = node[T][0]                     # 숫자 혹은 연산자
    left = node[T][1]
    right = node[T][2]
    exp = []

    if left == 0 and right == 0:        # 자식이 없을 때는 그냥 해당 노드의 값 반환
        return [ex]
    elif left != 0 and right == 0:      # 왼쪽만 있으면 왼쪽 탐색
        in_order(left)

    if T:
        exp += in_order(left)  # exp에 숫자, 연산자 담아두기
        exp += [ex]
        exp += in_order(right)

        if len(exp) == 3:                   # 리스트에 숫자-연산자-숫자가 됐을 때 연산하고 반환
            if exp[1] == '+':
                answer = exp[0] + exp[2]

            elif exp[1] == '-':
                answer = exp[0] - exp[2]

            elif exp[1] == '*':
                answer = exp[0] * exp[2]

            else:
                answer = exp[0] / exp[2]

            node[T][0] = answer  # 왼 + 오 값을 node에 기록
            return [answer]  # 연산한 값을 형제 노드랑 계산해야하므로 반환

    return [exp]


T = 10

for tc in range(1, 11):
    N = int(input())

    node = [[None, 0, 0] for _ in range(N+1)]          # idx: 노드 번호, [숫자, 왼쪽 번호, 오른쪽 번호]

    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            n, o, l, r = data
            n, l, r = int(n), int(l), int(r)
            node[n][0] = o
            node[n][1] = l
            node[n][2] = r
        else:
            n, num = data
            n, num = int(n), int(num)
            node[n][0] = num

    result = in_order(1)
    print(f'#{tc}',int(*result))