import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))     # a = list(str(input()))
    num = {}
    for number in a:
        if number in num.keys():
            num[number] += 1
        elif number == 0:
            pass
        else:
            num[number] = 1
    keys = num.keys()
    values = num.values()

    max_value = int(max(values))
    max_key = 0
    
    for key in keys:
        if num[key] == max_value:
            if max_key < key:
                max_key = key
    print(f'#{tc} {max_key} {max_value}')



