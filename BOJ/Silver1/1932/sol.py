N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]
# print(tree)

for i in range(1, N):
    for j in range(i+1):
        previous = 0
        if j == 0:
            previous = tree[i-1][0]
        elif j == i:
            previous = tree[i-1][-1]
        else:
            previous = max(tree[i-1][j-1], tree[i-1][j])
        tree[i][j] = tree[i][j] + previous
# print(tree)
print(max(tree[-1]))