import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N: 숫자 개수, K번째 큰 숫자
    num_list = list(input())    # 숫자(문자형) 리스트
    visited = set()             # 중복 제거를 위한 set

    # N // 4 만큼의 집합이 나옴, 중복은 제거
    for k in range(N//4):                                           # 회전 숫자만큼 반복
        num_list = [num_list[-1]] + num_list[0:len(num_list) - 1]   # 숫자 1칸씩 회전
        for i in range(0, N, N//4):                                 # 한 변에 있는 숫자들을 확인
            temp = num_list[i:i+N//4]
            num = ''
            for j in range(N//4):                 # 문자면 소문자로, 숫자면 그대로
                if temp[j].isupper():
                    num += temp[j].lower()
                else:
                    num += temp[j]

            num = int(num, 16)                    # 10진수로 변환해서 visited에 저장
            if num in visited:
                continue
            else:
                visited.add(num)

    s_set = sorted(visited, reverse=T)            # 내림차순 정렬
    print(f'#{tc} {s_set[K-1]}')
