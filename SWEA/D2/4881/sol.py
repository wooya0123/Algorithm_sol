import sys
sys.stdin = open('sample_input.txt')

def perm(arr, n):
    global min_total
    if n == N:
        total = 0
        for k in range(len(arr)):
            total += matrix[k][arr[k]]
        if min_total > total:
            min_total = total
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            arr.append(N_list[i])
            perm(arr, n + 1)
            arr.pop()
            used[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    N_list = [n for n in range(N)]
    min_total = 9999

    perm([], 0)
    print(f'#{tc} {min_total}')

