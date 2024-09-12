def solution(n, arr1, arr2):
    new_arr = [[0] * n for _ in range(n)]
    for i, num in enumerate(arr1):
        temp = bin(num)
        b_num = temp[2:]
        bin_num = ''
        if len(b_num) < n:
            bin_num = '0' * (n - len(b_num)) + b_num
        else:
            bin_num = b_num
        for x in range(n):
            if bin_num[x] == '1':
                new_arr[i][x] = '#'
            else:
                new_arr[i][x] = ' '

    for j, num in enumerate(arr2):
        temp2 = bin(num)
        b_num2 = temp2[2:]
        bin_num2 = ''
        if len(b_num2) < n:
            bin_num2 = '0' * (n - len(b_num2)) + b_num2
        else:
            bin_num2 = b_num2
        for y in range(n):
            if bin_num2[y] == '1' or new_arr[j][y] == '#':
                new_arr[j][y] = '#'

    ans = []
    for s in range(n):
        word = ''
        for e in range(n):
            word += new_arr[s][e]
        ans.append(word)

    return ans


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

ans = solution(n, arr1, arr2)
print(ans)