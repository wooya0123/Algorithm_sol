N = int(input())
honey_list = list(map(int, input().split()))

# case1. 벌(맨 왼쪽)-벌-꿀(맨 오른쪽)
case1_total = 0
for i in range(1, N):
    total = 0
    if i > 1:
        total = sum(honey_list[1:i-1])
    total += sum(honey_list[i+1:]) * 2
    if case1_total < total:
        case1_total = total

# case2. 벌(맨 왼쪽)-꿀-벌(맨 오른쪽)
case2_total = 0
for j in range(1, N-1):
    total = sum(honey_list[1:j+1])
    total += sum(honey_list[j:N-1])
    if case2_total < total:
        case2_total = total

# case3. 꿀(맨 왼쪽)-벌-벌(맨 오른쪽)
case3_total = 0
for k in range(1, len(honey_list)):
    total = sum(honey_list[:k]) * 2
    total += sum(honey_list[k+1:])
    if case3_total < total:
        case3_total = total

print(max(case1_total,case2_total,case3_total))