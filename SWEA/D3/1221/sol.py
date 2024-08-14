import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    number = list(map(str, input().split()))

    counts = [0] * 10
    temp = [0] * N

    for n in number:                # number에 숫자가 각 몇 개씩 있는지 세기
        if n == 'ZRO':
            counts[0] += 1
        elif n == 'ONE':
            counts[1] += 1
        elif n == 'TWO':
            counts[2] += 1
        elif n == 'THR':
            counts[3] += 1
        elif n == 'FOR':
            counts[4] += 1
        elif n == 'FIV':
            counts[5] += 1
        elif n == 'SIX':
            counts[6] += 1
        elif n == 'SVN':
            counts[7] += 1
        elif n == 'EGT':
            counts[8] += 1
        elif n == 'NIN':
            counts[9] += 1

    for i in range(1, len(counts)):             # 누적값으로 변환
        counts[i] += counts[i-1]

    for word in number:
        if word == 'ZRO':
            counts[0] -= 1
            idx = counts[0]
        elif word == 'ONE':
            counts[1] -= 1
            idx = counts[1]
        elif word == 'TWO':
            counts[2] -= 1
            idx = counts[2]
        elif word == 'THR':
            counts[3] -= 1
            idx = counts[3]
        elif word == 'FOR':
            counts[4] -= 1
            idx = counts[4]
        elif word == 'FIV':
            counts[5] -= 1
            idx = counts[5]
        elif word == 'SIX':
            counts[6] -= 1
            idx = counts[6]
        elif word == 'SVN':
            counts[7] -= 1
            idx = counts[7]
        elif word == 'EGT':
            counts[8] -= 1
            idx = counts[8]
        elif word == 'NIN':
            counts[9] -= 1
            idx = counts[9]

        temp[idx] = word
    print(tc)
    for s in temp:
        print(s, end=' ')
