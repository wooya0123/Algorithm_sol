import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N: 전체 과목 개수 K: 선택할 과목 개수
    scores = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if scores[j] < scores[j+1]:     # 내림차순 정렬
                scores[j], scores[j+1] = scores[j+1], scores[j]

    total = 0
    for k in range(K):
        total += scores[k]

    print(f'#{tc} {total}')