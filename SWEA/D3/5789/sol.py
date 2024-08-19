import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))      # N: 상자 개수 Q: 상자 번호 바꾸는 작업 횟수
    changes = [list(map(int, input().split())) for _ in range(Q)]   # 상자 번호 바꿀 때 L~R번을 range(Q)로 바꿈

    boxes = [0] * N     # 번호 기록할 박스들

    for i in range(Q):      # i+1 = Q 작업횟수
        l, r = changes[i]   # l번부터 r번까지 변경
        for k in range(l, r+1):
            boxes[k-1] = i+1    # k = 박스번호  ->  k-1 = boxes의 인덱스

    print(f'#{tc}',*boxes)

