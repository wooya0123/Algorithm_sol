# import sys
# sys.stdin = open('sample_input.txt')

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        # rank가 같으면 한쪽을 다른 쪽 아래로 병합하고 rank를 증가시킴
        parents[root_y] = root_x
        ranks[root_x] += 1


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 출석번호 마지막 번호, M: 신청서 수
    applicant = list(map(int, input().split()))     # 신청 현황 (2개씩 끊어서 보기)

    parents = list(range(0, N+1))
    ranks = [0] * (N+1)

    for i in range(M):
        # a가 b랑 같은 조 하고 싶다. a가 부모
        a = applicant[2*i]
        b = applicant[2*i+1]

        union(a, b)

    for j in range(len(parents)):
        parents[j] = find_set(j)

    check = set(parents[1:])
    print(f'#{tc} {len(check)}')

