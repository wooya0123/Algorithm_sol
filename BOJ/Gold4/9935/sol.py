import sys

words = sys.stdin.readline().rstrip()
bombs = list(sys.stdin.readline().rstrip())

stack = []

for word in words:
    # 문자열을 하나씩 스택에 추가
    stack.append(word)
    # 문자열 길이가 폭탄 길이랑 같아지면 검사
    if len(stack) >= len(bombs):
        # 스택 뒤에서부터 폭탄 길이만큼 확인해서 폭탄이랑 같으면 스택에서 빼기
        if stack[-len(bombs):] == bombs:
            for _ in range(len(bombs)):
                stack.pop()

# 스택을 문자열로 바꿔서 출력
res = ''.join(stack)
print(res if res else 'FRULA')


# 문자열로 풀이하면 시간초과 발생
# while True:
#     idx = words.find(bombs)
#     if idx == -1:
#         break
#     words = words[:idx] + words[idx+len(bombs):]
#
# if words:
#     print(words)
# else:
#     print('FRULA')

