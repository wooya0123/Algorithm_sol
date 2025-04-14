str1 = input()
str2 = input()
dp = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):