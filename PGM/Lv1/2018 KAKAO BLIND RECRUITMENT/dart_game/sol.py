def solution(dartResult):
    dartResult = dartResult.replace('10', 'k')      # 10을 판별하기 위해 k로 변경
    score = list(dartResult)
    temp = None
    ans = []

    for i in range(len(score)):
        if temp == None:                        # 처음에는 숫자 바로 넣기
            if score[i] == 'k':
                temp = 10
            elif score[i].isdigit():
                temp = int(score[i])
        else:
            if score[i] == 'k':                 # temp에 있던 숫자 ans에 넣고 temp에 새로운 숫자
                ans.append(temp)
                temp = 10
            elif score[i].isdigit():
                ans.append(temp)
                temp = int(score[i])
            else:                               # 문자열이면 temp 연산
                if score[i] == 'S':
                    continue
                elif score[i] == 'D':
                    temp = temp ** 2
                elif score[i] == 'T':
                    temp = temp ** 3
                elif score[i] == '#':
                    temp = temp * (-1)
                else:
                    if ans:                     # 별이면 ans 맨 마지막 숫자 2배, temp 2배
                        ans[-1] = ans[-1] * 2
                        temp = temp * 2
                    else:
                        temp = temp * 2

    # temp에 숫자 남았으면 다 ans에 넣어주기
    if temp:
        ans.append(temp)

    total = 0
    for num in ans:     # 숫자 꺼내면서 합산
        total += num

    return total

dartResult = '1S2D*3T'
res = solution(dartResult)
print(res)