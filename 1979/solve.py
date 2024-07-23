import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = (map(int, input().split()))  # N = 퍼즐 크기, K = 단어 길이
    for _ in range(N):
        row = list(map(int, input().split()))
        print(row)
        

'''
가로에서 먼저 3개 짜리 공간 확인
zip 함수로 세로로 묶은 후 3개짜리 공간 확인
'''