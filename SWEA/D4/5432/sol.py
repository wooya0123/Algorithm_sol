import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(str, input()))
    new_arr = []

    for k in range(len(arr)):
        if arr[k] == '(' and arr[k+1] == ')':
            new_arr += [0]
        elif arr[k] == ')' and arr[k-1] == '(':
            continue
        else:
            new_arr += arr[k]
    print(new_arr)



    sticks = [0] * 100
    stack = []
    point = 0

    for i in new_arr:
        if i == '(':

