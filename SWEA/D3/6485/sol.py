import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 주어질 버스 노선 개수
    line = [list(map(int, input().split())) for _ in range(N)]  # 각 노선이 다니는 버스 정류장 번호의 범위
    P = int(input())    # 확인하고 싶은 버스 정류장 개수
    station = [int(input()) for _ in range(P)]      # 확인하고 싶은 버스 정류장 번호들
    result = []

    for j in station:       # j는 버스정류장 번호
        cnt = 0             # 이 정류장에 다니는 노선 개수
        for k in line:      # k는 1개의 노선이 다니는 버스 정류장 번호의 범위
            if k[0] <= j <= k[1]:   # 버스정류장 번호가 해당 노선의 이동 범위에 속하면 cnt + 1
                cnt += 1
        result += [cnt]

    print(f'#{tc}', *result)