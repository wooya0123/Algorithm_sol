import sys
sys.stdin = open('input.txt')

def in_order(T):
    value = node[T][0]
    left = node[T][1]
    right = node[T][2]

    if T:
        in_order(left)
        print(value, end='')
        in_order(right)

T = 10

for tc in range(1, T+1):
    N = int(input())    # 트리가 갖는 노드의 수

    node = [[0, 0, 0] for _ in range(N+1)]    # idx: 노드 번호, 0: 노드 값, 1: 왼쪽, 2: 오른쪽

    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            n, v, l, r = data
            n, l, r = int(n), int(l), int(r)
            node[n][0] = v
            node[n][1] = l
            node[n][2] = r
        elif len(data) == 3:
            n, v, l = data
            n, l = int(n), int(l)
            node[n][0] = v
            node[n][1] = l
        else:
            n, v = data
            n = int(n)
            node[n][0] = v

    print(f'#{tc} ', end='')
    in_order(1)
    print()