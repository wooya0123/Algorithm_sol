import sys
sys.stdin = open('sample_input.txt')


def in_order(T, count):
    if T <= N:
        count = in_order(2*T, count)
        tree[T] = count
        count += 1
        count = in_order(2*T+1, count)
    return count

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)
    in_order(1, 1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')