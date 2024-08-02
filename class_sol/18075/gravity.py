import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = 0

    for i in range(N):
        max_fall = N - (i + 1)

        for j in range(i+1, N):
            if numbers[i] <= numbers[j]:
                max_fall -= 1

        if result < max_fall:
            result = max_fall

    print(f'#{tc} {result}')