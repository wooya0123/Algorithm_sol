N = int(input())

def counting_star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']  # n == 3일 때 모양

    star = counting_star(n//2)
    res = []

    for s in star:
        res.append(' '*(n//2) + s + ' '*(n//2))
    for s in star:
        res.append(s + ' ' + s)

    return res

print('\n'.join(counting_star(N)))