import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    sum_odd = 0
    row = list(map(int, input().split()))
    for num in row:
        if num % 2 == 1:
            sum_odd = sum_odd + num
    print(f'#{t+1} {sum_odd}')