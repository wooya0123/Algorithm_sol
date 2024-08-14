import sys
sys.stdin = open('sample_input.txt')
T = 10

# 해당 건물의 높이가 양 옆의 2개 건물들과 높이보다 높은지 판단하는 함수
def big(height, a, b, c, d):
    if height > a and height > b and height > c and height > d:
        return True


for tc in range(1, T+1):
    N = int(input())    # 건물 개수
    height = list(map(int, input().split()))
    # print(height)

    view = 0
    for i in range(2, N-2):
        if big(height[i], height[i+1], height[i+2], height[i-1], height[i-2]):
            lst = [height[i+2], height[i+1], height[i-1], height[i-2]]
            for x in range(3, 0, -1):
                for y in range(0, x):
                    if lst[y] > lst[y+1]:
                        lst[y], lst[y+1] = lst[y+1], lst[y]
            view += (height[i] - lst[-1])

    print(f'#{tc} {view}')

