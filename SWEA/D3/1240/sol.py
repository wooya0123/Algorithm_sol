import sys
sys.stdin = open('input.txt')

def is_correct(T):
    odd = 0         # 홀수 자리 숫자들만 더한 값
    even = 0        # 짝수 자리 숫자들만 더한 값
    for i in range(0, 8, 2):
        odd += int(T[i])
        even += int(T[i+1])
    num = odd + even
    if (odd * 3 + even) % 10 == 0:  # 올바른 암호인지 검증
        return num
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # M: 배열 가로크기, N: 배열 세로크기
    code = [input() for _ in range(N)]
    password = []           # 암호 저장
    num_password = ''       # 숫자 암호로 변환

    # 뒤에서부터 읽어서 1이 나오면 그 때부터 56개 저장
    for i in range(N):
        stop = 0
        for j in range(M-1, -1, -1):
            if code[i][j] == '1':
                for k in range(0, 56, 7):       # 1을 56번째 자리라 하고 0번째 자리부터 7개씩 끊어서 저장
                    password.append(code[i][j-56+1+k:j-56+1+k+7])
                stop = 1
                break
        if stop == 1:
            break

    # 암호를 숫자 암호로 변환
    for word in password:
        if word == '0001101':
            num_password += '0'
        elif word == '0011001':
            num_password += '1'
        elif word == '0010011':
            num_password += '2'
        elif word == '0111101':
            num_password += '3'
        elif word == '0100011':
            num_password += '4'
        elif word == '0110001':
            num_password += '5'
        elif word == '0101111':
            num_password += '6'
        elif word == '0111011':
            num_password += '7'
        elif word == '0110111':
            num_password += '8'
        elif word == '0001011':
            num_password += '9'

    result = is_correct(num_password)
    print(f'#{tc} {result}')


