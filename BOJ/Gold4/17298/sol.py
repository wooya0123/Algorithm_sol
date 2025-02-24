N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [-1] * N

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        ans[idx] = arr[i]
    stack.append(i)

for j in ans:
    print(j, end=" ")



# for i in range(len(arr)):
#     a = arr[i]
#     for j in range(i+1, len(arr)):
#         if arr[j] <= a:
#             pass
#         else:
#             print(arr[j], end=" ")
#             break
#     else:
#         print(-1, end=" ")
