import sys
sys.stdin = open('sample_input.txt')

def post_order(T):
    num = node[T][0]
    left = node[T][1]
    right = node[T][2]
    res = []

    if left == 0 and right == 0:        # 자식이 없을 때는 그냥 해당 노드의 값 반환
        return [num]
    elif left != 0 and right == 0:      # 왼쪽만 있으면 왼쪽 탐색
        post_order(left)

    if T:
        res += post_order(left)         # res에 숫자 담아두기
        res += post_order(right)
        answer = res[0] + res[1]
        node[T][0] = answer             # 왼 + 오 값을 node에 기록
        return [answer]                 # 연산한 값을 형제 노드랑 계산해야하므로 반환

    return [num]




T = int(input())

for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))       # N: 노드 개수, M: 리프 노드 개수, L: 출력할 노드 번호

    node = [[0, 0, 0] for _ in range(N+1)]        # idx 노드 번호, [숫자, 왼쪽 번호, 오른쪽 번호]

    for _ in range(M):
        n, num = list(map(int, input().split()))    # n: 노드 번호, num: 노드에 들어갈 수
        node[n][0] = num

    for i in range(1, (N+1)//2 +1):
        node[i][1] = 2*i if 2*i <= N else 0
        node[i][2] = 2*i+1 if 2*i + 1 <= N else 0

    post_order(1)
    print(f'#{tc} {node[L][0]}')