'''
600,000 글자 입력 가능
맨 처음에는 커서는 문장 맨 뒤에 위치
모든 명령어 수행 후 편집기에 입력되어 있는 문자열 수
문자열 길이: N
영어 소문자로만
입력할 명령어: M
셋째 줄부터 M개의 줄에 걸쳐 명령어
'''

import sys
from collections import deque

sentence = sys.stdin.readline().rstrip()

front = deque()
back = deque()

for i in range(len(sentence)):
    front.append(sentence[i])
M = int(sys.stdin.readline().rstrip())  # 명령어 개수
# cursor = len(sentence)

for i in range(M):
    command = sys.stdin.readline().rstrip().split()

    # 문자 입력 명령어
    if len(command) == 2:
        front.append(command[1])

        # sentence = sentence[:cursor] + command[1] + sentence[cursor:]
        # cursor += 1

    # 삭제
    elif command[0] == 'B':
        if front:
            front.pop()

        # if cursor > 0:
            # sentence = sentence[:cursor - 1] + sentence[cursor:]
            # cursor -= 1

    # 왼쪽 이동
    elif command[0] == 'L':
        if front:
            word = front.pop()
            back.appendleft(word)

    # 오른쪽 이동
    elif command[0] == 'D':
        if back:
            word = back.popleft()
            front.append(word)

# 리스트를 문자열로
res1 = ''.join(front)
res2 = ''.join(back)
res = res1 + res2

print(res)