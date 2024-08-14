import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()

    result = []
    if len(word) % 2 == 0:
        play = int(len(word) / 2)
    else:
        play = int((len(word) - 1) / 2)

    for i in range(play):
        if word[i] == word[-(i+1)]:
            result += [True]
        else:
            result += [False]

    if False in result:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
