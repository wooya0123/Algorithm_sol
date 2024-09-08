import sys
sys.stdin = open('sample_input.txt')

def dfs(month, cost):
    global ans
    # 종료 조건 - 12월까지 탐색했으면 종료
    if month > 12:
        ans = min(ans, cost)
        return

    # 각 달은 4가지의 경우가 있음
    # 1일권으로 구매
    dfs(month + 1, cost + arr[month] * d1)

    # 1달권 구매
    dfs(month + 1, cost + m1)

    # 3달권 구매
    dfs(month + 3, cost + m3)

    # 1년권 구매
    dfs(month + 12, cost + y1)


T = int(input())

for tc in range(1, T+1):
    d1, m1, m3, y1 = list(map(int, input().split()))    # 이용권 가격
    arr = [0] + list(map(int, input().split()))  # 12개월 계획
    ans = 1e9

    dfs(1, 0)
    print(f'#{tc} {ans}')