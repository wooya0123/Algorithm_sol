def solution(info, edges):
    V = len(info)       # 노드 수
    E = len(edges)      # 간선 수
    G = [[0, 0] for _ in range(V)]      # 부모 노드(idx)의 자식 노드 저장
    # visited = [0] * V

    for edge in edges:                  # 인접 리스트 생성
        if G[edge[0]][0] == 0:
            G[edge[0]][0] = edge[1]
        else:
            G[edge[0]][1] = edge[1]

    max_sheep = 0

    def DFS(current, sheep, wolf, possible_nodes, visited):
        nonlocal max_sheep
        # 해당 노드의 동물 체크
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1

        # 종료 조건
        if sheep <= wolf:
            return
        else:
            if max_sheep < sheep:
                max_sheep = sheep

        # 현재 정점의 자식 정점 추가 (가본 적이 없는 노드만 추가)
        new_possible_nodes = possible_nodes + [node for node in G[current] if node not in visited]

        # 이동 가능한 정점들을 순회하며 재귀 호출
        for next in new_possible_nodes:
            next_possible_nodes = new_possible_nodes.copy()     # 복사한 노드 리스트 전달
            next_possible_nodes.remove(next)                    # 복사한 노드 리스트에서 다음 갈 노드는 제외하고 전달
            DFS(next, sheep, wolf, next_possible_nodes, visited + [next])   # visited에 방문 노드 추가하고 전달


    DFS(0, 0, 0, [], [0])

    return max_sheep

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))