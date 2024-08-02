import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 11):
    dump = int(input())
    g_height = list(map(int, input().split()))

    result = 0
    for _ in range(dump):      # 덤프 제한 횟수만큼 반복
        max_height = 1         # max, min 값은 덤프할 때마다 초기화
        min_height = 100
        # 가장 높은 곳의 높이와 가장 낮은 곳의 높이를 찾는다
        for i in range(len(g_height)):
            if max_height <= g_height[i]:
                max_height = g_height[i]
            if min_height >= g_height[i]:
                min_height = g_height[i]
        # 가장 높은 곳의 상자의 개수를 -1, 가장 낮은 곳의 상자의 개수를 +1
        for m in range(len(g_height)):
            if g_height[m] == max_height:
                g_height[m] -= 1
                break                       # 찾은 첫 번째 값을 조정하고 break
        for n in range(len(g_height)):
            if g_height[n] == min_height:
                g_height[n] += 1
                break                       # 찾은 첫 번째 값을 조정하고 break
    
    # 모든 작업을 마친 후 최종적으로 max, min 값을 업데이트
    max_height = 1
    min_height = 100
    for i in range(len(g_height)):
        if max_height <= g_height[i]:
            max_height = g_height[i]
        if min_height >= g_height[i]:
            min_height = g_height[i]

    result = max_height - min_height
    print(f'#{tc} {result}')
