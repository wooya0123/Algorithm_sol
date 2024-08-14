import sys
sys.stdin = open('input.txt')


def create_password(numbers):
    password = numbers + [None]
    qsize = len(password)       # 크기 9

    front = 0
    rear = 8

    while password[rear] != 0:
        for i in range(1, 6):       # 1 ~ 5까지 빼기 (1 사이클)
            password[rear] = password[front] - i    # front 값에서 i를 빼고 rear에 넣기
            password[front] = None          # 디버깅용 - front 값을 뺏으면 None 할당
            if password[rear] <= 0:         # rear가 0이나 음수면 0으로 할당하고 반복문 종료
                password[rear] = 0
                break
            rear = (rear + 1) % qsize       # 인덱스는 다음 인덱스 값을 배열 크기로 나눈 나머지를 할당
            front = (front + 1) % qsize

    if front < rear:                # front가 None이므로 그 다음부터 끝까지
        return password[front+1:]
    else:                           # front가 None이므로 그 다음부터 끝까지, rear까지 포함해야하므로 rear+1까지
        return password[front+1:] + password[:rear+1]


T = 10

for tc in range(1, 11):
    N = int(input())
    numbers = list(map(int, input().split()))

    password = create_password(numbers)
    print(f'#{tc}', *password)