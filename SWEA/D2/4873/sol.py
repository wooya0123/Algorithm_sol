import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    words = list(map(str, input()))
    # print(word)

    stack = []
    for word in words:
        if not stack:
            stack.append(word)
        elif stack[-1] != word:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
    result = len(stack)

    print(f'#{tc} {result}')