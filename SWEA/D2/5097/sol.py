import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    li = list(map(int, input().split())) + [0] * (M+1)

    front = 0
    rear = N
    for _ in range(M):
        li[rear] = li[front]
        front += 1
        rear += 1
    print(f'#{tc} {li[front]}')