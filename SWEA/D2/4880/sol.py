import sys
sys.stdin = open('sample_input.txt')

result = {
    (1, 3) : 'left',
    (2, 1) : 'left',
    (3, 2) : 'left',
    (3, 1) : 'right',
    (1, 2) : 'right',
    (2, 3) : 'right',
    (1, 1) : 'left',
    (2, 2) : 'left',
    (3, 3) : 'left'
}


def f(i, j):  # i~j번까지의 승자를 찾는 함수
    if i == j:  # 한 명만 남은 경우
        return i
    else:  # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i + j) // 2)  # 왼쪽 그룹의 승자
        right = f((i + j) // 2 + 1, j)  # 오른쪽 그룹의 승자
        return win(left, right)  # 두 그룹의 승자를 찾는 함수 구현

def win(left, right):
    res = result[(player[left], player[right])]
    if res == 'left':
        return left
    else:
        return right



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    player = [0] + list(map(int, input().split()))
    winner = f(1, N)
    print(f'#{tc} {winner}')



