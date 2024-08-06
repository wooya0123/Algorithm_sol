import sys
sys.stdin = open('input.txt')

T = int(input())

def istotal_zero(arr):
    subsets = [[]]
    # 부분 집합 모두 구하기
    for x in arr:                               # arr의 원소를 가져와서
        for i in range(len(subsets)):           # subset의 길이만큼 반복하면서(subset의 길이는 계속 변함, 아래에서 값이 계속 추가되기 때문)
                subsets += [subsets[i] + [x]]   # subset의 원소에 arr의 원소를 추가한 리스트를 append

    for s in subsets:                           # 중복 허용하지 않는 부분집합
        s.sort()                                # 리스트는 순서가 있기 때문에 중복을 제거하지 위해 모든 리스트의 값을 정렬

    new_subsets = []                            # 새로운 subset에 중복된 부분집합 제외하고 추가
    for ss in subsets:
        if not ss:                              # 처음에 들어가는 공집합을 제거하기 위한 조건
            continue
        elif ss not in new_subsets:
            new_subsets += [ss]

    cnt = 0
    for subset in new_subsets:                  # 부분집합의 값을 가져와서 합이 0인 경우만 세어 출력
        total = 0
        for sss in subset:
            total += sss
        if total == 0:
            cnt += 1

    if cnt == 0:
        return 0
    else:
        return 1

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    result = istotal_zero(arr)

    print(f'#{tc} {result}')



