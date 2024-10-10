# 옷 개수! - 옷 종류C옷 종류
import itertools

def solution(clothes):
    clothes_type = [[clothes[0][1], 0]]

    for cloth in clothes:
        tp = cloth[1]
        for cloth_type in clothes_type:
            if tp == cloth_type[0]:
                cloth_type[1] += 1
                break
        else:
            clothes_type.append([tp, 1])
    print(clothes_type)

    k = 1                               # 입는 옷의 갯수
    res = len(clothes)                  # 처음에는 옷을 1개씩 입을 때
    while k < len(clothes_type):
        k += 1
        groups = itertools.combinations(clothes_type, k)    # 조합할 옷 종류 개수만큼 조합 생성
        for group in groups:                                # 옷 종류 조합에서 각 종류의 옷 개수만큼 곱해주기
            total = 1
            for g in group:
                total *= g[1]
            res += total

    return res

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))