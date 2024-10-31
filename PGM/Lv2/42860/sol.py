# 폐기한 풀이

def solution(name):
    move = 0
    change = []
    alph = [0] * len(name)

    for i in range(len(name)):
        # 알파벳 변경(13번 부터는 뒤에서 세는 게 더 빠름)
        c = ord(name[i]) - 65
        if c <= 13:
            change.append(c)
        else:
            # change.append(90 - ord(n))
            change.append(90 - ord(name[i]))

        # 이동할 배열 생성
        if name[i] == 'A':
            alph[i] = 0
        else:
            alph[i] = 1

    current = 0
    while True:
        right = 0
        left = 0
        for r in alph[current+1:] + alph[:current]:
            if r == 0:
                right += 1
            else:
                right += 1
                break
        for l in alph[:current] + alph[current+1:]:
            if l == 0:
                left += 1
            else:
                left += 1
                break



    return move

name = "JEROEN"
print(solution(name))