import sys
sys.stdin = open('sample_input.txt')

def quick_sort(left, right):
    if left < right:
        pivot = partition(left, right)
        quick_sort(left, pivot-1)       # 받아온 피봇값의 인덱스 기준 왼/오를 다시 정렬
        quick_sort(pivot+1, right)

def partition(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]                            # 피봇값은 중간값으로
    arr[left], arr[mid] = arr[mid], arr[left]   # 피봇값을 왼쪽으로 보내고 시작
    i = left + 1
    j = right

    while i <= j:                               # i랑 j가 교차될 때까지 진행
        while i <= j and arr[i] <= pivot:       # 왼쪽에서부터 피봇보다 작은 값 찾기
            i += 1
        while i <= j and arr[j] >= pivot:       # 오른쪽에서부터 피봇보다 큰 값 찾기
            j -= 1
        if i < j:                               # i와 j가 교차되지 않았는데 멈췄으면 두 값을 바꿔줘서 while문 다시 진행
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]       # j - i 순서로 교차됐으면 i는 피봇보다 큰 수, j는 피봇보다 작은 수이므로 제일 왼쪽의 피봇값을 j자리로 바꾸기
    return j    # 피봇값의 idx를 반환

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 정수 개수
    arr = list(map(int, input().split()))

    quick_sort(0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')
