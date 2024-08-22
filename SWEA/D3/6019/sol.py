import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    # D: 기차 사이 거리, A: A기차 속력, B: B기차 속력, F: 파리 속력
    D, A, B, F = list(map(int, input().split()))

    h = D / (A + B)     # 기차가 충돌하기 전까지 시간
    fly_distance = F * h   # 그 시간만큼 파리가 움직인 거리

    print(f'#{tc} {fly_distance}')

    # chance = 1
    # # 기차 사이 거리 업데이트
    # train_interval = D
    # fly_distance = 0
    # while train_interval > 1e-10:
    #     if chance % 2 == 1:         # A -> B로 이동
    #         h = train_interval / 35     # 파리가 이동한 시간
    #         fly_distance += 20 * h      # 파리가 이동한 거리
    #         train_interval -= 25 * h    # h 시간 후 기차 사이 간격 조정
    #         chance += 1
    #
    #     elif chance % 2 == 0:       # B -> A로 이동
    #         h = train_interval / 30     # 파리가 이동한 시간
    #         fly_distance += 20 * h      # 파리가 이동한 거리
    #         train_interval -= 25 * h    # h 시간 후 기차 사이 간격 조정
    #         chance += 1
    #
    # print(f'#{tc} {fly_distance: 10f}')



