import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x                # 자기 자신이 대표 원소일 때까지 탐색

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))      # V+1: 노드 개수, E: 간선 개수
    edge = [list(map(int, input().split())) for _ in range(E)]     # (노드1, 노드2, 가중치)
    edge.sort(key=lambda x: x[2])       # 가중치 기준 오름차순 정렬
    parent = [i for i in range(V+1)]    # 처음에는 자기 자신이 대표 원소

    cnt = 0
    total = 0       # 가중치의 합

    for n1, n2, w in edge:
        if find_set(n1) != find_set(n2):
            cnt += 1
            total += w
            parent[find_set(n2)] = find_set(n1)

            if cnt == V:    # 노드 개수 - 1 만큼 간선을 확인하면 종료
                break

    print(f'#{tc} {total}')
