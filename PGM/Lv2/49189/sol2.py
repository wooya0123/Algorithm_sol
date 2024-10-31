from collections import deque

def solution(n, edge):
    # 인접리스트 생성
    nodes = [[] for _ in range(n+1)]
    for v in edge:
        nodes[v[0]].append(v[1])
        nodes[v[1]].append(v[0])

    q = deque()                 # 덱 사용
    q.append((1,1))             # (노드 번호, 1번 노드로부터 거리)
    distance = [0] * (n+1)      # 노드 거리 체크할 리스트
    distance[1] = 1             # 1번 노드 거리 1로 저장

    while q:
        node, cnt = q.popleft()

        # 해당 노드에서 갈 수 있는 노드를 덱에 저장, distance에 체크
        for next_node in nodes[node]:
            if distance[next_node] == 0:
                q.append((next_node, cnt+1))
                distance[next_node] = cnt+1

    max_edge = max(distance)
    res = distance.count(max_edge)      # 가장 먼 노드의 개수 세기
    return res

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))