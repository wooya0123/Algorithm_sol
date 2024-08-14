import sys
sys.stdin = open('sample_input.txt')

T = int(input())



for tc in range(1, T+1):

    N = int(input())        # N은 칠할 영역
    red_index = []
    blue_index = []


    for _ in range(N):
        paint = list(map(int, input().split()))     # 영역 칠하기 N번째
        
        purple = 0      # 보라색 칸의 개수

        # 색이 빨간색인 경우 빨간색에 해당하는 칸의 좌표를 모두 리스트에 담기
        if paint[-1] == 1:
            for i in range(paint[0], paint[2]+1):
                for j in range(paint[1], paint[3]+1):
                        red_index += [[i, j]]

        # 색이 파란색인 경우 파란색 해당하는 칸의 좌표를 모두 리스트에 담기
        elif paint[-1] == 2:
            for i in range(paint[0], paint[2]+1):
                for j in range(paint[1], paint[3]+1):
                        blue_index += [[i, j]]

    # 만약 red_index에 있는 값이 blue_index에도 있다면 count에 1 증가
    for r in red_index:
        if r in blue_index:
            purple += 1

    print(f'#{tc} {purple}')



