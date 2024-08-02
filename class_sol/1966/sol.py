import sys
sys.stdin = open('input.txt')

T = int(input())

def bubble_sort(num, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

def selection_sort(num, N):
    for i in range(N-1):            # 배열의 맨 끝자리만 빼고
        min_idx = i                 # 최솟값으로 삼을 값의 인덱스를 i로 설정
        for j in range(i + 1, N):   # i 이후의 값과 비교해서 i보다 작으면 자리 바꾸기
            if num[min_idx] > num[j]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]

def counting_sort(num, N):
    max_num = 0                     # num에서 최댓값 찾기
    for n in num:
        if n > max_num:
            max_num = n

    counts = [0] * (max_num + 1)    # num의 가장 큰 수만큼 빈 공간
    temp = [0] * N                  # num의 길이만큼 빈 공간
    for number in num:              # num값을 index로 하는 counts 공간에 +1
        counts[number] += 1

    for i in range(1, len(counts)):  # counts 값을 누적값으로 변환
        counts[i] += counts[i - 1]

    for i in num:
        counts[i] -= 1              # counts의 누적 값을 1감소
        temp[counts[i]] = i         # counts의 값이 i값의 인덱스, 그 자리에 i 삽입

    return temp

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    bubble_sort(num, N)
    selection_sort(num, N)
    # sorted_num = counting_sort(num, N)

    result = ' '.join(map(str, num))
    # result = ' '.join(map(str, sorted_num))

    print(f'#{tc} {result}')