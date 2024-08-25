import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    N = -1

    for word in words:
        if N < len(word):
            N = len(word)
    result = ''

    for i in range(N):
        for j in range(N):
            try:
                result += words[j][i]

            except IndexError as error:
                result += ''
    print(f'#{tc} {result}')
