import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    s, k = list(input().split())
    k = int(k)
    # print(s, k)

    if s == 'o..' :
        if k == 0:
            print(f'#{tc} 0')
        elif k % 2 == 0:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')

    elif s == '.o.':
        if k == 0:
            print(f'#{tc} 1')
        elif k % 2 == 0:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')

    elif s == '..o':
        if k == 0:
            print(f'#{tc} 2')
        elif k % 2 == 0:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')
        
    


# def possible_case(s, k):
#     possibility = [s]
#     for _ in range(k):
#         if 'o..' in possibility:
#             possibility.append('.o.')

#         elif '.o.' in possibility:
            
#             possibility.append('o..')

#         elif '..o' in possibility:
#             possibility.append('.o.')
    
#     left = possibility.count('o..')
#     middle = possibility.count('.o.')
#     right = possibility.count('..o')
    
#     if left >= middle and left >= right:
#         return 0
#     elif left < middle and middle >= right:
#         return 1
#     elif left < right and middle < right:
#         return 2