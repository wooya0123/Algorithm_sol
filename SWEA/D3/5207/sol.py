import sys
sys.stdin = open('sample_input.txt')

def bin_search(low, high, target, lr):
    if low > high:                                          # 다 탐색했는데 못 찾았으면 -1 반환
        return -1

    mid = (low + high) // 2

    if target == a_lst[mid]:                                # 앞의 조건들에 걸리지 않고 찾았으면 1 반환
        return 1
    elif target < a_lst[mid]:                               # 찾으려는 수가 왼쪽에 있는데
        if lr == 's' or lr == 'r':                          # 첫 번째 시도거나 이전에 오른쪽을 보고 왔다면 탐색
            return bin_search(low, mid-1, target, 'l')
        else:
            return -1
    else:                                                   # 찾으려는 수가 오른쪽에 있는데
        if lr == 's' or lr == 'l':                          # 첫 번재 시도거나 이전에 왼쪽을 보고 왔다면 탐색
            return bin_search(mid+1, high, target, 'r')
        else:
            return -1

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: A에 속한 정수 개수, M: B에 속한 정수 개수
    a_lst = list(map(int, input().split()))     # 여기서 찾을 예정
    a_lst = sorted(a_lst)
    b_lst = list(map(int, input().split()))     # 이 수들이 a리스트에 있는지 확인할 예정

    lr = 's'
    cnt = 0

    for x in b_lst:
        result = bin_search(0, len(a_lst) - 1, x, lr)
        if result == 1:     # 1인 경우만 세기
            cnt += 1
    print(f'#{tc} {cnt}')


