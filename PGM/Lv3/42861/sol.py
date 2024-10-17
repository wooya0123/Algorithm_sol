from heapq import heappush, heappop
# heap은 가중치가 최소인 값을 맨 앞에 저장, heappop하면 앞에서부터 꺼내옴

def solution(n, costs):
    V = n               # 노드 개수
    E = len(costs)      # 간선 개수
    graph = [[0] * V for _ in range(V)]     # 가중치 무방향 그래프 생성
    for cost in costs:
        u, v, w = cost
        graph[u][v] = w
        graph[v][u] = w

    def prim(start):
        heap = list()
        MST = [0] * V       # 노드 개수만큼 트리 생성

        sum_weight = 0

        # heappush(힙 리스트, (가중치, 노드))
        heappush(heap, (0, start))      # 노드 0에 가중치 0으로 시작

        while heap:
            weight, v = heappop(heap)   # weight: 가중치, v: 노드

            if MST[v]:              # 방문했던 노드라면 continue
                continue
            MST[v] = 1              # 해당 노드 방문처리
            sum_weight += weight    # 현재 꺼내온 노드가 최소 가중치이므로 가중치 합에 더하기

            for next in range(V):   # 해당 노드에서 다음 노드로 연결된 게 있으면 힙에 추가
                if graph[v][next] == 0:
                    continue
                heappush(heap, (graph[v][next], next))
        return sum_weight

    return prim(0)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))
