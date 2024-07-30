import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(str(input()))
    num = {}
    for i in a:
        if i in num.keys():
            num[i] += 1
        elif i == 0:
            pass
        else:
            num[i] = 1
    keys = num.keys()
    values = num.values()
    
    max_value = int(max(values))
    max_key = 0
    key = 0
    for key in keys:
        if num[key] == max_value:
            if keys[j] > keys[j+1]:
                max_key = keys[j]
    print(f'#{tc} {max_key} {max_value}')

    

