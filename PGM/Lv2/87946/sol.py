# 유저가 탐험할 수 있는 최대 던전 수 찾기
# (최소 필요 피로도, 소모 피로도)

import itertools

def solution(k, dungeons):
    max_cnt = 0
    for dungeon in itertools.permutations(dungeons, len(dungeons)):     # 순열 만들어서 순서대로 던전 배열
        current = k
        cnt = 0
        for dg in dungeon:
            if current >= dg[0]:    # 남은 피로도가 최소 필요도보다 높으면 던전 입장, 카운트
                current -= dg[1]
                cnt += 1
            else:                   # 던전 못 들어가면 break
                break
        if max_cnt < cnt:
            max_cnt = cnt

    return max_cnt

k = 80
dungeons = [[80,20],[50,40],[30,10]]
res = solution(k, dungeons)
print(res)