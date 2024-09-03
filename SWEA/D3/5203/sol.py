import sys
sys.stdin = open('sample_input.txt')

def play(arr):
    arr = sorted(arr)
    n = len(arr)
    res = None

    # run
    # 카드 1개 기준 다음 카드들 중 같은 것이 있으면 cnt + 1, cnt가 3이상이면 run
    for i in range(0, n-2):
        cnt = 0
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt >= 2:
            res = 'r'
            break
    if res:                 # run을 찾았으면 triplet 찾지 않도록 설정
        return res

    # triplet
    # 조합 만들기 -> 조합 만들어서 연속된 숫자면 triplet
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

    # 받는 카드 정보 저장
    p1 = [0] * 6
    p2 = [0] * 6
    for i in range(0, 12, 2):
        p1[i//2] = draw[i]
        p2[i//2] = draw[i+1]

    # 각 턴에 p1과 p2가 받는 카드를 turn1과 turn2에 저장
    winner = None
    turn1 = [p1[0], p1[1]]      # 카드 3개 이상부터 비교할 것이므로 미리 2개 넣어둠
    turn2 = [p2[0], p2[1]]
    for j in range(2, 6):
        turn1.append(p1[j])     # 카드 하나 뽑고 시작
        result = play(turn1)       # run, triplet 확인
        if result:
            winner = 1
            break

        turn2.append(p2[j])     # p2 확인
        result = play(turn2)
        if result:
            winner = 2
            break

    # 승자 있으면 승자 출력, 무승부면 0 출력
    if winner:
        print(f'#{tc} {winner}')
    else:
        print(f'#{tc} {0}')