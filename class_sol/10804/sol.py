import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()

    new_word =''

    for i in range(len(word)-1, -1, -1):
        if word[i] == 'b':
            new_word += 'd'
        elif word[i] == 'd':
            new_word += 'b'
        elif word[i] == 'p':
            new_word += 'q'
        elif word[i] == 'q':
            new_word += 'p'
    print(f'#{tc} {new_word}')