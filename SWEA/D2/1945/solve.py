import sys
sys.stdin = open('input.txt')

T = int(input())

# 2로 나누고 나머지가 0이면 카운트 +1, N을 2로 나눈 몫을 N에 할당,
# 나머지가 0이 아니면 break 
# 과정 반복


for tc in range(1, T+1):
    N = int(input())
    # 2로 나눌 경우
    a = 0
    while 2 <= N:
        if N % 2 == 0:
            a += 1
            N = N / 2
        else:
            break

    # 3로 나눌 경우        
    b = 0
    while 3 <= N:
        if N % 3 == 0:
            b += 1
            N = N / 3
        else:
            break

    # 5로 나눌 경우
    c = 0
    while 5 <= N:
        if N % 5 == 0:
            c += 1
            N = N / 5
        else:
            break

    # 7로 나눌 경우
    d = 0
    while 7 <= N:
        if N % 7 == 0:
            d += 1
            N = N / 7
        else:
            break

    # 11로 나눌 경우
    e = 0
    while 11 <= N:
        if N % 11 == 0:
            e += 1
            N = N / 11
        else:
            break

print(f'#{tc} {a} {b} {c} {d} {e}')