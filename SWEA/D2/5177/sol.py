import sys
sys.stdin = open('sample_input.txt')

def enq(num):
    global last
    last += 1                       # 마지막 노드를 한 칸 밀어줌
    h[last] = num                   # 힙의 마지막 노드 자리에 배열할 숫자를 넣어줌
    c = last                        # 비교할 자식 번호: 마지막 노드
    p = c//2                        # 비교할 부모 번호: 마지막 노드의 부모 번호
    while p >= 1 and h[p] > h[c]:   # 부모 번호가 루트가 아니고 부모가 자식보다 크면 자리 바꿈
        h[p], h[c] = h[c], h[p]
        c = p                       # 자리 바꿨으니 비교할 자식 번호 -> 부모 번호로
        p = c//2                    # 바뀐 자식 번호의 부모 번호로 갱신

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    h = [0] * (N+1)
    last = 0            # 마지막 노드

    for num in arr:
        enq(num)

    res = 0

    i = last // 2
    while i >= 1:       # 루트 노드 번호까지 조사했으면 중단
        res += h[i]
        i = i//2

    print(f'#{tc} {res}')