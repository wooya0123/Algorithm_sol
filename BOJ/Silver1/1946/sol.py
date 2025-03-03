T = int(input())

for _ in range(T):
    N = int(input())
    # [서류심사 성적 순위, 면접 성적 순위]
    scores = [list(map(int, input().split())) for n in range(N)]

    scores.sort(key=lambda x: x[0])
    cnt = 1     # 서류 1등 뽑기
    min_score = scores[0][1]    # 서류 1등의 면접 순위 기준

    # 다음 볼 사람은 서류가 이전 사람보다 낮으므로 면접 순위가 이전보다 높아야함
    for score in scores:
        if score[1] < min_score:
            cnt += 1
            min_score = score[1]    # 다음 사람은 뽑힌 사람보다 순위 높아야 함
    print(cnt)