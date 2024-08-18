import sys
sys.stdin = open('sample_input.txt')

T = 10

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        x = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
        if buildings[i] > x:
            result += (buildings[i] - x)

    print(f'#{tc} {result}')