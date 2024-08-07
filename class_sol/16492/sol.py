import sys
sys.stdin = open('sample_input.txt')

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [10] * (N // 10)
    if N % 2 == 0:
        arr += [20] * (N // 20)
    else:
        arr += [20] * ((N-1) // 20)
    # print(arr)

    subsets = [[]]

    for x in arr:
        for i in range(len(subsets)):
            if len(subsets[i] + [x]) <= N // 10 and subsets[i] + [x] not in subsets:
                subsets.append(subsets[i] + [x])

    blocks =[]
    for subset in subsets:  # 부분집합의 값을 가져와서 합이 N인 경우만 새롭게 구성
        total = 0
        for sss in subset:
            total += sss
        if total == N:
            blocks += [subset]
    # print('its', blocks)

    cnt = 0
    for block in blocks:
        num_of_10 = 0
        num_of_20 = 0
        for n in block:
            if n == 10:
                num_of_10 += 1
            elif n == 20:
                num_of_20 += 1

        if num_of_10 != 0 and num_of_20 != 0:
            cnt += factorial(len(block)) / (factorial(num_of_10) * factorial(num_of_20)) * (2 ** num_of_20)
        elif num_of_10 == 0:
            cnt += 2 ** num_of_20
        elif num_of_20 == 0:
            cnt += 1

    result = int(cnt)
    print(f'#{tc} {result}')