import sys
sys.stdin = open('sample_input.txt')

def merge_sort(m):
    global cnt

    if len(m) == 1:
        return m

    mid = len(m) // 2   # 반 갈라서 왼/오 나누기
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)     # 한 쪽 배열을 함수를 돌려서 다시 반으로 쪼개기
    right = merge_sort(right)

    if left[-1] > right[-1]:    # 2개로 쪼개졌을 때 교수님이 요구하신 거 체크하기
        cnt += 1

    return merge(left, right)   # 합쳐진 배열을 왼/오에 반환해주기

def merge(left, right):
    result = [0] * (len(left) + len(right))             # 정렬된 리스트 반환할 거
    l_idx = r_idx = 0

    while l_idx < len(left) and r_idx < len(right):     # 왼/오 리스트에서 작은 거부터 result에 집어넣기
        if left[l_idx] < right[r_idx]:
            result[l_idx + r_idx] = left[l_idx]
            l_idx += 1
        else:
            result[l_idx + r_idx] = right[r_idx]
            r_idx += 1

    while l_idx < len(left):                            # 한 쪽 다 넣었으면 반대쪽 남은 거 다 넣어주기
        result[l_idx + r_idx] = left[l_idx]
        l_idx += 1

    while r_idx < len(right):
        result[l_idx + r_idx] = right[r_idx]
        r_idx += 1

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N: 정수의 개수
    arr = list(map(int, input().split()))
    cnt = 0

    res = merge_sort(arr)
    print(f'#{tc} {res[N//2]} {cnt}')