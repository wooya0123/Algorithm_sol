import sys
sys.stdin = open('input.txt')

def card_change(cnt):
    global answer
    if cnt == C:                    # 카드 교환 횟수만큼 했다면 최댓값인지 확인
        temp = int(''.join(card))
        if answer < temp:
            answer = temp
        return

    # 완전 탐색
    # 앞 카드와 뒷 카드를 교환 -> 재귀를 통해 교환 횟수만큼 교환 -> visited에 해당 배열 저장
    # 카드를 교환 후 확인하여 해당 배열을 확인한 적이 있다면 더 이상 보지 않음
    for i in range(len(card)-1):
        for j in range(i+1, len(card)):
            card[i], card[j] = card[j], card[i]

            current = ''.join(card)
            if (cnt, current) in visited:
                pass
            else:
                card_change(cnt + 1)
                visited.append((cnt, current))

            card[i], card[j] = card[j], card[i]

T = int(input())

for tc in range(1, T+1):
    *card, C = input().split()    # card: 숫자카드 배열(str), C: 교환 횟수
    card = list(card[0])
    C = int(C)
    visited = []
    answer = 0

    card_change(0)

    print(f'#{tc} {answer}')