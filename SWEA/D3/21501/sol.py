import sys
sys.stdin = open('sample_input.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

subsets = [[]]
for x in A:
    for i in range(len(subsets)):
        subset = subsets[i] + [x]
        if subset not in subsets:
            subsets += [subset]

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    cnt = 0
    for ss in subsets:
        if len(ss) == N:
            total = 0
            for sss in ss:
                total += sss
            if total == K:
                cnt += 1

    print(f'#{tc} {cnt}')
