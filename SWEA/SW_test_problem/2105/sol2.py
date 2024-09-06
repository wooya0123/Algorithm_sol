import sys
sys.stdin = open('sample_input.txt')

def DFS(si, sj, x, y, k, path):     # 출발 x좌표, 출발 y좌표, 현재 x좌표, 현재 y좌표, 현재까지 경로
    global res
    # 기저 조건
    if si == x and sj == y and path:    # 현재 지점이 출발 지점으로 돌아왔고 현재 지점에서 이동한 게 아니면
        res.add(len(path))              # 경로의 길이를 저장

    # 다음 재귀 호출 전
    if x < si or y < 0 or x >=N or y >= N or arr[x][y] in path:     # 격자를 벗어나지 않고, 마지막 방향 바꿨을 때 x가 변을 뚫고 가면 종료
        return

    dir = [(1,1), (1,-1), (-1,-1), (-1,1)]

    path.append(arr[x][y])
    nx = x + dir[k][0]
    ny = y + dir[k][1]

    # 재귀 호출
    DFS(si, sj, nx, ny, k, path)        # 모든 게 ok면 해당 방향으로 직진

    if k == 3:                          # 마지막 방향으로 쭉 가다가 처음 지점을 못 만나고 쭉 가면 결국엔 return 되어 종료됨
        DFS(si, sj, nx, ny, 0, path)
    else:
        DFS(si, sj, nx, ny, k+1, path)  # 안 되는 경우를 만나면 방향을 바꾸기

    # 재귀 호출하고 돌아왔을 때
    path.pop()                          # 방향도 바꿔서 갔는데도 안 되는 걸 만나면 후진(해당 점을 path에서 빼기)

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 격자 크기 N * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = set()
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            DFS(i, j, i, j, 0, [])

    if res:
        print(f'#{tc} {max(res)}')
    else:
        print(f'#{tc} -1')