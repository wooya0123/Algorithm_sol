import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]

    row = list(map(str, input().split()))
    year = row[0][0:4]
    month = row[0][4:6]
    int_month = int(row[0][5:6])
    day = row[0][6:8]
    int_day = int(row[0][7:8])

    # print(year)
    if int_month in day_31 and 1 <= int_day <= 31:
        print(f'#{t+1} {year}/{month}/{day}')
    elif int_month in day_30 and 1 <= int_day <= 30:
        print(f'#{t+1} {year}/{month}/{day}')
    elif int_month == 2 and 1 <= int_day <= 28:
        print(f'#{t+1} {year}/{month}/{day}')
    else:
        print(f'#{t+1} -1')