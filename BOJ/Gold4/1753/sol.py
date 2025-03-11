import heapq

V, E = list(map(int, input().split())) # 정점, 간선
K = int(input()) # 시작 노드

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))

distances = [float('inf')] * (V+1)
distances[K] = 0

q = [(0, K)] # 거리, 도착 노드
visited = set()

while q:
    current_distance, current_node = heapq.heappop(q)

    # 방문한 곳은 패스
    if current_node in visited:
        continue

    # 방문 안 한 곳은 방문 처리
    visited.add(current_node)

    # 다음 갈 곳
    for next, weight in graph[current_node]:
        distance = current_distance + weight

        if distance < distances[next]:
            distances[next] = distance
            heapq.heappush(q, (distance, next))

for i in range(1, V+1):
    if distances[i] == float('inf'):
        print('INF')
        continue
    print(distances[i])
