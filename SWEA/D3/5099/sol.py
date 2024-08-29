import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N: 화덕 크기, M: 피자 개수
    C_list = list(map(int, input().split()))    # Ci: i번째 피자의 치즈 양
    oven = [0] * N
    made = 0

    for j in range(len(C_list)):            # [피자번호, 치즈 양]
        C_list[j] = [j+1, C_list[j]]

    # 초기에 화덕에 피자 넣기
    for i in range(N):
        oven[i] = C_list[i]

    # 피자를 1개 빼고 다 만들면 종료
    while made < M-1:
        for p in range(len(oven)):              # 화덕 1바퀴 돌리기
            if made == M-1:                     # 피자를 1개 빼고 다 만들었으면 break
                break
            if oven[p]:                         # 화덕 자리에 피자가 있으면
                oven[p][1] = oven[p][1] // 2    # 피자의 녹지 않은 치즈 양을 절반으로
                if oven[p][1] == 0:             # 치즈가 다 녹았으면
                    made += 1                   # 다 만들었다고 체크
                    if made <= M-N:             # 아직 만들 피자가 남았으면
                        oven[p] = C_list[N-1+made]  # 그 자리에 새로운 피자 넣기
                    else:
                        oven[p] = None          # 더 만들 피자 없으면 화덕 자리에 None

    for pizza in oven:
        if pizza:
            print(f'#{tc} {pizza[0]}')          # 1개 남은 피자 번호 출력
