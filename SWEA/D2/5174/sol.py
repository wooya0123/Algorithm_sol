import sys
sys.stdin = open('sample_input.txt')

def cnt_node(N):
    cnt = 0
    if N != 0:
        cnt += cnt_node(left[N])
        cnt += cnt_node(right[N])
        cnt += 1
        return cnt

    return 0

T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))      # E: 간선, N: 루트 노드
    arr = list(map(int, input().split()))       # 부모 자식 순서

    left = [0] * (E+2)      # 0 고려한 노드 개수 만큼
    right = [0] * (E+2)
    # node = [0] * (E+2)

    for i in range(0, len(arr), 2):
        if left[arr[i]] == 0:
            left[arr[i]] = arr[i+1]
        else:
            right[arr[i]] += arr[i+1]


    print(f'#{tc} {cnt_node(N)}')
