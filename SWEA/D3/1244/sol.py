# import sys
# sys.stdin = open('input.txt')

def card_change(cnt, lst):
    if cnt == C:
        return

    if cnt >= len(lst)-1:                           # 1개 빼고 정렬됐을 때
        card[-1], card[-2] = card[-2], card[-1]     # 맨 뒤에 2개만 계속 바꾸기
        res = card_change(cnt+1, lst)
    else:
        lst = card[cnt:]
        max_num = max(lst)
        # 정렬할 리스트의 맨 앞에 최고 숫자가 아닐 때 뒤에서부터 탐색해서 최고 숫자를 맨 앞으로
        if lst[0] != max_num:
            for i in range(len(lst)-1, cnt-1, -1):
                if card[i] == max_num and card[cnt] != card[i]:
                    card[cnt], card[i] = card[i], card[cnt]
                    res = card_change(cnt+1, card[cnt:])
                    break
        else:
            new_lst = lst[1:]
            card_change(cnt, new_lst)
    return res


T = int(input())

for tc in range(1, T+1):
    *card, change = input().split()    # card: 숫자카드 배열, change: 교환 횟수
    card = list(map(int, card[0]))
    C = int(change)
    visited = [0] * len(card)

    print(f'#{tc} {card_change(0, card)}')