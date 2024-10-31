def solution(name):
    move = 0
    alph = [0] * len(name)

    for i in range(len(name)):
        # 알파벳 변경(13번 부터는 뒤에서 세는 게 더 빠름)
        c = ord(name[i]) - 65
        if c <= 13:
            move += c
        else:
            move += (90 - ord(name[i]))

        # 이동할 배열 생성
        if name[i] != 'A':
            alph[i] = 1

    # 정방향
    right = 0
    right_a = 0
    for x in range(1, len(alph)):
        right += 1
        if alph[x] == 1:
            for j in range(x, len(alph)):
                if alph[j] == 1:
                    right_a += 1
                else:
                    break
            break

    # 역방향
    left = 0
    left_a = 0
    return

name = "JEROEN"
print(solution(name))