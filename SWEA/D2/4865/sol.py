import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = set(map(str, input()))
    str2 = list(map(str, input()))

    # print(str1)
    # print(str2)
    word_dict = {}                                  # 키(문자): 값(횟수)
    for word in str2:
        if word in str1 and word not in word_dict:
            word_dict[word] = 1
        elif word in str1 and word in word_dict:
            word_dict[word] += 1

    max_value = 0                       # 딕셔너리에서 가장 높은 값 찾기
    for w in word_dict.values():
        if max_value < w:
            max_value = w

    print(f'#{tc} {max_value}')