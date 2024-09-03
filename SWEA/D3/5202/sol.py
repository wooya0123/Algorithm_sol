import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 신청서 개수
    schedule = [tuple(map(int, input().split())) for _ in range(N)]     # (시작 시간, 종료 시간)
    schedule.sort(key=lambda x: x[1])

    time = schedule[0][1]       # 현재 시간: 첫 번째 화물 작업 종료 시간으로 설정
    res = 1                     # 첫 번째 화물 카운트
    for truck in schedule:
        if truck[0] >= time:    # 작업 시작 시간이 현재 시간보다 빠르면
            time = truck[1]     # 시간을 화물 다 나른 시간으로 변경
            res += 1

    print(f'#{tc} {res}')