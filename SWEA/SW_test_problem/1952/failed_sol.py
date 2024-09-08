import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    d1, m1, m3, y1 = list(map(int, input().split()))    # 이용권 가격
    arr = list(map(int, input().split()))  # 12개월 계획
    swim = 0

    use_m1 = m1 / d1    # 며칠이면 1일권보다 1달권이 이득인지
    use_m3 = (m1 * 3) / m3    # 몇 달이면 1달권보다 3달권이 이득인지

    # 0이 아닌 부분만 떼서 확인
    f = 0
    b = 0
    for k in range(len(arr)):
        if arr[k] != 0:
            f = k
            break
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] != 0:
            b = j
            break
    schedule = arr[f:b+1]
    ans = 0

    for i in range(len(schedule)):
        if i < len(schedule) - 2:

            if schedule[i] != 0:
                # 3개씩 끊어서 보기
                cost = 99999
                sc = [schedule[i], schedule[i+1], schedule[i+2]]
                # 1일권 + 1달권
                case1 = 0
                for x in sc:
                    if x >= use_m1:
                        case1 += m1
                    else:
                        case1 += d1
                if cost > case1:
                    cost = case1
                # 3달권
                if cost > m3:
                    cost = m3

                ans = cost
                schedule[i] = schedule[i+1] = schedule[i+2] = 0

    print(ans)









