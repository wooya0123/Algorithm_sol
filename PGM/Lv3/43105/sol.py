def solution(triangle):
    k = 0
    while k < len(triangle)-1:
        k += 1
        for i in range(k+1):
            if i == 0:
                triangle[k][i] += triangle[k - 1][i]
            elif i == k:
                triangle[k][i] += triangle[k - 1][i - 1]
            else:
                v1 = triangle[k][i] + triangle[k - 1][i - 1]
                v2 = triangle[k][i] + triangle[k - 1][i]
                if v1 < v2:
                    triangle[k][i] = v2
                else:
                    triangle[k][i] = v1

    res = max(triangle[-1])
    return res

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
ans = solution(triangle)
print(ans)