import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def special_sort(arr, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    new_arr = []
    for i in range(N):
        j = (N-1) - i
        if len(new_arr) >= 10:
            break
        if i < j:
            new_arr += [arr[j], arr[i]]
        else:
            break


    return new_arr


for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    result = special_sort(number, N)

    print('#', end='')
    print(tc, end=' ')
    for num in result:
        print(num, end = ' ')
    print()


