import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = list(map(str, input()))

    for i in range(len(str2) - len(str1) + 1):
        new_word = ''
        for j in range(len(str1)):
            new_word += str2[i+j]
        if new_word == str1:
            print(f'#{tc} 1')
            break

        if i == len(str2) - len(str1):
            if new_word != str1:
                print(f'#{tc} 0')

