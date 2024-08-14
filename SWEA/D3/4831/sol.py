import sys
sys.stdin = open('sample_input.txt')

# # K만큼 이동하고 그 곳에 충전기가 없으면 뒤로 후진
# def drive(end):
#     start = 0
#     while start < end:
#         arrival = start + K
#         if arrival < 0:
#             return 0
#         if arrival >= end:
#             return
#         elif stations[arrival] == 1:
#             stations[arrival] += 10
#             start = arrival
#             continue
#         else:
#             while stations[arrival] != 1:
#                 arrival -= 1
#             if stations[arrival] == 1:
#                 stations[arrival] += 10
#                 start = arrival

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    station_num = list(map(int, input().split()))

    stations = [0] * (N+1)

    # 버스 정류장 리스트를 만들고 충전기가 있는 곳은 1로 표시
    for i in station_num:
        stations[i] = 1

    # 츨발지점부터 종점까지 while문 반복
    start = 0
    while start < N:
        arrival = start + K     # 버스가 도착한 지점
        if arrival >= N:        # 버스가 이동한 곳이 종점이거나 넘어갔으면 종료
            break
        elif stations[arrival] == 1:    # 충전기가 있는 정류장이면 10을 더해주고 도착지점 변경
            stations[arrival] += 10
            start = arrival
            continue
        else:
            k = 0
            while k != K and stations[arrival] != 1:    # 버스가 이동할 수 있는 거리 k만큼 충전기가 있을 때까지 후진
                k += 1
                arrival -= 1
            if stations[arrival] == 1:      # 이동한 곳에 충전기가 있으면 10 더해줌
                stations[arrival] += 10
                start = arrival
            elif stations[arrival] == 11:   # 이동한 곳에 이미 왔던 곳이면 10 더해서 체크
                stations[arrival] += 10
                start = arrival
        if 21 in stations:      # 만약 2번 온 적이 있으면 못 가는 걸로 판단하고 종료
            break

    # 충전기 정류장 방문한 횟수 세기
    charge_cnt = 0
    for num in stations:
        if num == 11:
            charge_cnt += 1
        elif num == 21:
            charge_cnt = 0
            break
    print(f'#{tc} {charge_cnt}')

