import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # N: 컨테이너 수, M: 트럭 수
    freight_list = list(map(int, input().split()))   # 화물별 무게
    capacity_list = list(map(int, input().split()))  # 트럭 적재용량
    res = 0

    freight_list.sort(reverse=T)    # 내림차순 정렬
    capacity_list.sort(reverse=T)

    for freight in freight_list:
        for i in range(len(capacity_list)):
            if capacity_list[i] >= freight:     # 화물 무게보다 적재용량이 크면 싣기
                res += freight
                capacity_list[i] = -1
                break
    print(f'#{tc} {res}')
