import sys
sys.stdin = open('sample_input.txt')

def BFS(S, G):
    queue = [S]
    visited[S] = 1

    while queue:
        current = queue.pop(0)
        if current == G:
            return visited[current] - 1
        for next in range(1, V+1):
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                queue.append(next)
                visited[next] = visited[current] + 1

    return 0



T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))      # V: 노드 개수 E: 간선 개수
    edge_info = [list(map(int, input().split())) for _ in range(E)]     # 간선 정보 [[i, j], ...]
    S, G = list(map(int, input().split()))      # S: 출발노드 G: 도착노드

    visited = [0] * (V+1)       # 방문 표시할 배열

    adj_matrix = [[0] * (V+1) for _ in range(V+1)]       # 인접행렬 초기화
    for i in range(0, len(edge_info)):
        n1, n2 = edge_info[i]
        adj_matrix[n1][n2] = adj_matrix[n2][n1] = 1           # 무방향이므로 current -> next 양방향 모두 1

    result = BFS(S, G)
    print(f'#{tc} {result}')