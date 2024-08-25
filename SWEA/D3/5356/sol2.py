import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    max_len = -1
    result = ''

    for word in words:
        if max_len < len(word):
            max_len = len(word)

    for i in range(max_len):
        for word in words:
            if i < len(word):
                result += word[i]
    print(result)