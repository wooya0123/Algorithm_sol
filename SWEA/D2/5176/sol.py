import sys
sys.stdin = open('sample_input.txt')

def in_order(T):
    if T:
        in_order(left[T])
        node.append(T)
        in_order(right[T])

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    node = []               # 중위순회할 때 노드 번호
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    res = [0] * (N + 1)     # idx: 노드 번호, value: 해당 노드에 들어가는 값

    for i in range(1, N//2 + 1):
        left[i] = i*2
        right[i] = i*2 + 1 if i*2 + 1 <= N else 0

    in_order(1)

    for j in range(len(node)):
        res[node[j]] = j+1

    print(f'#{tc} {res[1]} {res[N//2]}')