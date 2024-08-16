import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))   # N: 자격 있는 사람 수, M초 동안 K개 만듦
    customer = list(map(int, input().split()))

    # 고객 리스트 오름차순 정렬
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if customer[j] > customer[j+1]:
                customer[j], customer[j+1] = customer[j+1], customer[j]

    made = 0
    sold = 0
    time = 0
    fail = 0

    for visit in customer:
        if visit > time:        # 현재 시간이 방문시간보다 작으면
            time = visit        # 현재 시간을 방문시간으로 바꿈
            made = visit // M * K - sold    # 남은 붕어빵 개수 = 현재 시간까지 만들 수 있는 붕어빵 개수  - 팔린 붕어빵 개수

        if made > 0:        # 만들어진 붕어빵 개수가 0보다 크면 하나 빼고 팔렸다고 표시
            made -= 1
            sold += 1
        elif made <= 0:     # 만들어진 붕어빵이 없으면 실패라고 표시
            fail += 1
            break
    if fail > 0:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')