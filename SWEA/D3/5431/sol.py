import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N: 수강생 수 K: 제출한 사람 수
    submit = list(map(int, input().split()))
    entire = [n for n in range(1, N+1)]
    not_submit = []

    for o in submit:
        entire[o-1] = 0

    for x in entire:
        if x != 0:
            not_submit += [x]

    print(f'#{tc}', *not_submit)


