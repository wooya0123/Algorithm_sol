# 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 문자열은 두 글자씩 끊어서 다중집합의 원소
# 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
# "AB"와 "Ab", "ab"는 같은 원소
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

def solution(str1, str2):
    group1 = []
    group2 = []

    # 영어 문자열이면 넣기
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            group1.append(str1[i].upper() + str1[i+1].upper())

    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            group2.append(str2[j].upper() + str2[j+1].upper())


    union = []
    intsc = []
    for x in range(len(group1)):
        for y in range(len(group2)):
            if group1[x] == group2[y]:      # 교집합 만들기
                intsc.append(group1[x])
                group2[y] = 0
                break
        union.append(group1[x])             # 동시에 합집합 만들기
        group1[x] = 0

    for k in group2:                        # 교집합에 속하지 않은 group2 요소를 다 합집합에 넣어주기
        if k != 0:
            union.append(k)

    if len(union) == 0:                 # 분모가 0일 때는 1
        j = 1
    else:                               # 아니면 나누기
        j = len(intsc) / len(union)

    ans = int(j * 65536)                # 소수점 버리기

    return ans


str1 = 'FRANCE'
str2 = 'french'
res = solution(str1, str2)
print(res)