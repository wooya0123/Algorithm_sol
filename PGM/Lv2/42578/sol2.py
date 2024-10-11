def solution(clothes):
    # {옷 종류: 옷 개수} 형태로 딕셔너리 생성
    dict_clothes = {}
    for val, key in clothes:
        if key in dict_clothes.keys():
            dict_clothes[key] += 1
        else:
            dict_clothes.update({key: 1})

    # 해당 옷을 안 입는 경우를 고려해 각 옷 개수 +1 한 값을 곱해줌
    answer = 1
    for val_cnt in dict_clothes.values():
        answer *= val_cnt + 1

    # 옷을 전부 안 입는 경우 1가지를 빼줌
    answer -= 1


    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))