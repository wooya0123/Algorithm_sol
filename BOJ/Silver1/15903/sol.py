n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

for _ in range(m):
    fusion = num[0] + num[1]
    num[0] = fusion
    num[1] = fusion
    num.sort()
print(sum(num))
