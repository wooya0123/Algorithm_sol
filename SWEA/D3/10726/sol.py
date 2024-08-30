import sys
sys.stdin = open('input.txt')


def binary(num):
    temp = ''
    while num >= 0:
        if num % 2 == 1:
            num = num // 2
            temp += '1'
        else:
            num = num // 2
            temp += '0'

        if num == 0:
            break

    res = temp[::-1]
    return res

def is_correct(num, N):
    mask = (1 << N) - 1                 # N개 만큼 1로 채워진 이진수
    if (num & mask) == mask:
        return True
    else:
        False

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # M의 이진수 마지막 N개 비트가 모두 1인지

    if is_correct(M, N):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')