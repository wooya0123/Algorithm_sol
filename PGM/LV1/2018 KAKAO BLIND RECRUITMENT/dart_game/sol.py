def solution(dartResult):
    score = list(dartResult)
    temp = 0        # 연산할 숫자     # 현재 점수 저장
    res = []        # 현재까지 총합
    for s in score:
        if s.isdigit():
            if not temp:
                temp = int(s)
            else:
                res.append(temp)
        else:
            if s == 'S':
                continue
            elif s == 'D':
                current = current ** 2
            elif s == 'T':
                current = current ** 3
            elif s == '#':
                current = current * (-1)
            else:
                if res:
                    x = res.pop()
                    num = (x + temp) * 2
                    res.append(num)
                else:
                    num = temp * 2
                    res.append(num)

    if temp:
        res.append(temp)

    ans = 0
    for i in res:
        ans += i
    return ans