import sys
sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    # 간선 표시용 매트릭스 생성
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = list(map(int, input().split()))
        adj_matrix[n1][n2] = 1                      # 방향이 있기 때문에 current -> next 이 부분에만 간선 체크

    # S는 시작지점, G는 도착지점
    S, G = list(map(int, input().split()))

    # DFS로 이동하는데 출발지점 S에서 시작, 도착지점 G가 방문이 됐다면 경로가 있는 걸로 출력
    stack = [S]
    visited = [0] * (V + 1)

    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1

        for next in range(1, V + 1):
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                stack.append(next)
    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

