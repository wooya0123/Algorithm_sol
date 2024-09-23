def solution(name, yearning, photo):
    res =[]
    for pic in photo:
        total = 0
        for p in pic:
            for i in range(len(name)):
                if name[i] == p:
                    total += yearning[i]
                    break
        res.append(total)
    return res

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
answer = solution(name, yearning, photo)
print(answer)