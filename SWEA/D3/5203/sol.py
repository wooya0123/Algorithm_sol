import sys
sys.stdin = open('sample_input.txt')

def play(arr):
    arr = sorted(arr)
    n = len(arr)
    res = None
    if n >= 3:
        # run
        for i in range(0, n-2):
            cnt = 0
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    cnt += 1
            if cnt >= 2:
                res = 'r'
                break

        # triplet
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + 1 == arr[j] and arr[j] + 1 == arr[k]:
                        res = 't'
                        break
                if res:
                    break
            if res:
                break
    return res

T = int(input())

for tc in range(1, T+1):
    draw = list(map(int, input().split()))
    p1 = [0] * 6
    p2 = [0] * 6
    for i in range(0, 12, 2):
        p1[i//2] = draw[i]
        p2[i//2] = draw[i+1]

    winner = None
    turn1 = [p1[0], p1[1]]
    turn2 = [p2[0], p2[1]]
    for j in range(2, 6):
        turn1.append(p1[j])
        res = play(turn1)
        if res:
            winner = 1
            break

        turn2.append(p2[j])
        res = play(turn2)
        if res:
            winner = 2
            break
    if winner:
        print(f'#{tc} {winner}')
    else:
        print(f'#{tc} {0}')