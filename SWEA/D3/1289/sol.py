import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    bit = input()                   # 만들어야 하는 상태
    reset = '0' * len(bit)          # 초기 상태
    cnt = 0                         # 바꿔야 하는 횟수

    for i in range(len(bit)):
        if bit[i] != reset[i]:      # 만약 초기 상태의 숫자와 만들어야하는 상태의 숫자가 다르면
            num = bit[i]
            reset = reset[:i]       # 해당 부분까지 슬라이싱
            n = len(bit[i:])
            reset += (num * n)      # reset의 뒷부분을 바꾼 숫자로 다 바꾸기
            cnt += 1                # 바꾼 횟수 카운트

    print(f'#{tc} {cnt}')
