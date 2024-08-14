import sys
sys.stdin = open('input.txt')

T = int(input())    # 테스트 케이스 갯수

# 테스트 케이스의 1개 열에 1이 K개 연속으로 나오는지 확인하는 함수
    # 리스트 요소가 1이면 cnt를 1 증가
    # cnt가 K와 같다면(= 빈 공간이 단어 길이 만큼 있다) sc를 1 증가
    # cnt가 K보다 크다면(= 빈 공간이 단어 길이보다 많다) sc를 1 감소, cnt를 0으로
    # 리스트 요소가 1이 아니면 cnt는 0
def words_repetition(lst, K):                
    cnt = 0
    sc = 0
    
    for i in range(len(lst)):   
        if lst[i] == 1:
            cnt += 1                  
            if cnt == K:
                sc += 1
            elif cnt > K:
                sc -= 1
                cnt = 0
        else:
            cnt = 0
    if lst == [1] * len(lst) and len(lst) % (K + 1) == 1:   # 예외 케이스: 요소가 1밖에 없어서 sc가 0이어야 하지만 1이 되는 경우
        sc = 0
    return sc


for tc in range(1, T+1):
    success_case = 0
    N, K = (map(int, input().split()))  # N = 퍼즐 크기, K = 단어 길이
    

    lst_group = []     # 테스트 케이스를 열별로 담을 리스트
    for _ in range(N):
        row = list(map(int, input().split()))   # 테스트 케이스의 1개 열
        lst_group.append(row)                   # 1개 열을 리스트에 담기

        sc = words_repetition(row, K)      # K개의 빈 공간이 연속으로 있다면
        success_case = success_case + sc        # 성공 케이스 숫자 + 1
    for line in zip(*lst_group):                # 열별로 담은 리스트를 행으로 변환
        sc = words_repetition(line, K)       # K개의 빈 공간이 연속으로 있다면
        success_case = success_case + sc        # 성공 케이스 숫자 + 1
    print(f'#{tc} {success_case}')