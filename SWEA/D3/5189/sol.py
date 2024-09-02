import sys
sys.stdin = open('sample_input.txt')

def sp_perm(cnt, list):
    if cnt == len(arr):
        perm_list.append(list[:])
        return
    for i, val in enumerate(arr):
        if visited[i] == 1:
            continue
        else:
            list.append(val)
            visited[i] = 1

            sp_perm(cnt+1, list)

            list.pop()
            visited[i] = 0

        if visited[0] != 1:     # 처음에 사무실에서 출발하지 않는 경우는 제외
            break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    battery_map = [list(map(int, input().split())) for _ in range(N)]

    arr = range(N)
    visited = [0] * N
    perm_list = []      # 가능한 경로 저장
    res = 99999

    sp_perm(0, [])

    # 가능한 루트별로 배터리 소모 체크 후 최솟값 출력
    for j in range(len(perm_list)):
        route = perm_list[j] + [0]
        cnt = 0
        i = 0
        while i + 1 <= N:
            cnt += battery_map[route[i]][route[i + 1]]
            i += 1
        if res > cnt:
            res = cnt

    print(f'#{tc} {res}')