import sys
sys.stdin = open('input.txt')

T = int(input())    # 테스트 케이스 갯수

def three_words_repetition(lst, K):    # 테스트 케이스의 1개 열에 1이 K개 연속으로 나오는지 확인하는 함수            
    for i in range(len(lst) - (K-1)):   
        if lst[i] == lst[i+1] == lst[i+2]:
            if i + K < len(lst) and lst[i+K] == 1:
                return False
            return True
    return False

for tc in range(1, T+1):
    success_case = 0
    N, K = (map(int, input().split()))  # N = 퍼즐 크기, K = 단어 길이
    

    lst_group = []     # 테스트 케이스를 열별로 담을 리스트
    for _ in range(N):
        
        row = list(map(int, input().split()))   # 테스트 케이스의 한 열
        lst_group.append(row)                   # 한 열을 리스트에 담기

        if three_words_repetition(row, K):         # K개의 빈 공간이 연속으로 있다면
            success_case = success_case + 1     # 성공 케이스 숫자 + 1
    for line in zip(*lst_group):                # 열을 행으로 변환
        if three_words_repetition(line):
            success_case = success_case + 1
    print(f'#{tc} {success_case}')

'''
가로에서 먼저 3개 짜리 공간 확인
zip 함수로 세로로 묶은 후 3개짜리 공간 확인
'''