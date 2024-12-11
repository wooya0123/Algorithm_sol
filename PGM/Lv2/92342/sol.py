from itertools import combinations_with_replacement


def solution(n, info):
    max_gap = 0
    ans = [-1]

    # 라이언이 쏠 수 있는 모든 경우의 수(중복 허용 조합)
    for combination in combinations_with_replacement(range(11), n):
        ryan_info = [0] * 11
        for i in combination:
            ryan_info[i] += 1

        ryan_score = 0
        apeach_score = 0

        # 점수 계산
        for i in range(11):
            if ryan_info[i] > info[i]:  # 라이언이 이긴 경우
                ryan_score += 10 - i
            elif info[i] > 0:           # 어피치가 이긴 경우
                apeach_score += 10 - i

        gap = ryan_score - apeach_score

        if gap > max_gap:
            max_gap = gap
            ans = ryan_info
        elif gap == max_gap and gap > 0:            # 점수 차이가 같은 경우
            for i in range(10, -1, -1):
                if ryan_info[i] > ans[i]:
                    ans = ryan_info
                    break
                if ryan_info[i] < ans[i]:
                    break

    return ans

# 테스트 케이스
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

print(solution(n, info))