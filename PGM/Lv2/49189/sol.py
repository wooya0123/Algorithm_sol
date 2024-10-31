# 실패한 풀이 - DFS로 접근하려 했음

def solution(n, edge):
    nodes = [[] for _ in range(n+1)]
    for v in edge:
        nodes[v[0]].append(v[1])
        nodes[v[1]].append(v[0])
    print(nodes)

    max_cnt = 1

    def DFS(idx, visited, cnt):
        nonlocal max_cnt
        # 종료 조건
        # 갱신
        if max_cnt < cnt:
            max_cnt = cnt
        # 탐색
        for next_node in nodes[idx]:
            if next_node not in visited:
                DFS(next_node, visited+[next_node], cnt+1)

    DFS(1, [1], 1)


    return max_cnt

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))