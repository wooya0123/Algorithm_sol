row, col = list(map(int, input().split()))      # 블록 가로, 세로
N = int(input())        # 상점 개수
store = [list(map(int, input().split())) for _ in range(N)]     # (동서남북, 경계로부터 거리)
dong = list(map(int, input().split()))      # 동근의 위치(동서남북, 경계로부터 거리)

total = 0
for s in store:
    if dong[0] == 1:    # 동근이가 북쪽
        if s[0] == 1:
            total += abs(dong[1] - s[1])
        elif s[0] == 2:
            temp1 = (row - dong[1]) + col + (row - s[1])
            temp2 = dong[1] + col + s[1]
            total += min(temp1, temp2)
        elif s[0] == 3:
            total += dong[1] + s[1]
        else:
            total += (row - dong[1]) + s[1]

    elif dong[0] == 2:    # 동근이가 남쪽
        if s[0] == 1:
            temp1 = (row - dong[1]) + col + (row - s[1])
            temp2 = dong[1] + col + s[1]
            total += min(temp1, temp2)
        elif s[0] == 2:
            total += abs(dong[1] - s[1])
        elif s[0] == 3:
            total += dong[1] + (col - s[1])
        else:
            total += (row - dong[1]) + (col - s[1])

    elif dong[0] == 3:    # 동근이가 서쪽
        if s[0] == 1:
            total += dong[1] - s[1]
        elif s[0] == 2:
            total += (col - dong[1]) + s[1]
        elif s[0] == 3:
            total += abs(dong[1] - s[1])
        else:
            temp1 = (col - dong[1]) + row + (col - s[1])
            temp2 = dong[1] + row + s[1]
            total += min(temp1, temp2)

    elif dong[0] == 4:    # 동근이가 동쪽
        if s[0] == 1:
            total += dong[1] - (row - s[1])
        elif s[0] == 2:
            total += (col - dong[1]) + (row - s[1])
        elif s[0] == 3:
            temp1 = (col - dong[1]) + row + (col - s[1])
            temp2 = dong[1] + row + s[1]
            total += min(temp1, temp2)
        else:
            total += abs(dong[1] - s[1])
print(total)