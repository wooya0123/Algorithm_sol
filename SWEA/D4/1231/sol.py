import sys
sys.stdin = open('input.txt')

def in_order(T):
    result = ''
    if T:
        result += in_order(left[T])     # 왼쪽 먼저 탐색
        result += word[T]               # 더 이상 왼쪽에 값이 없으면 해당 노드의 단어를 result에 넣고 오른쪽 보기
        result += in_order(right[T])    # 오른쪽 노드로 이동해서 없으면 0이면 그냥 반환 -> 지금까지 result 가지고 부모 노드로, 있으면 해당 노드의 왼쪽부터 다시 보기

    return result

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x:int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]      # 노드번호, 노드문자, 연결된 노드

    left = [0] * (N+1)      # idx 0 고려해서 생성
    right = [0] * (N+1)
    word = [0] * (N+1)      # 각 노드의 단어를 기록할 리스트

    for x in arr:
        word[x[0]] = x[1]   # 리스트에서 단어는 idx 맞춰서 word에 기록
        if len(x) == 4:     # 리스트에 left, right 정보가 다 있으면 둘 다 기록
            left[x[0]] = x[2]
            right[x[0]] = x[3]

        elif len(x) == 3:   # 리스트에 left 정보만 있으면 left만 기록
            left[x[0]] = x[2]

    print(f'#{tc} {in_order(1)}')       # root는 1