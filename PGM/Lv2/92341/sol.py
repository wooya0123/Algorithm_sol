def solution(fees, records):
    parkinglot = []             # 입차 관리 리스트(차 번호, 입차 시간)
    parking_records = []        # 주차 시간 리스트(차 번호, 주차된 시간)
    for record in records:
        time, car_number, history = record.split()
        if history == 'IN':
            parkinglot.append((car_number, time))
        elif history == 'OUT':
            # 입차 관리 리스트 순회하면서 주차 시간 리스트에 주차 시간 저장
            for i in range(len(parkinglot)):
                if car_number == parkinglot[i][0]:
                    intime_h, intime_m = map(int, parkinglot[i][1].split(':'))
                    outtime_h, outtime_m = map(int, time.split(':'))
                    parking_time = (outtime_h - intime_h) * 60 + (outtime_m - intime_m)

                    # 한 번 주차했던 차라면 기존 시간에 추가하기
                    for parking_record in parking_records:
                        if car_number == parking_record[0]:
                            parking_record[1] += parking_time
                            break
                    # 온 적이 없는 차라면 리스트에 추가하기
                    else:
                        parking_records.append([car_number, parking_time])
                    parkinglot[i] = (0, 0)      # 구분하기 위해 다른 값 채워넣기
                    break

    # 출차 기록이 없는 차를 찾기 위해 입차 관리 리스트 순회 -> 23:59에 나간 걸로 계산 -> 주차 시간 리스트에 추가
    for rest in parkinglot:
        if rest[0] != 0:
            car_number = rest[0]
            intime_h, intime_m = map(int, rest[1].split(':'))
            parking_time = (23 - intime_h) * 60 + (59 - intime_m)
            for parking_record in parking_records:
                if car_number == parking_record[0]:
                    parking_record[1] += parking_time
                    break
            else:
                parking_records.append([car_number, parking_time])

    # 차 번호 기준으로 오름차순 정렬
    parking_records.sort(key=lambda x: x[0])

    # 주차한 차 요금 계산해서 res 리스트에 추가
    res = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    for car in parking_records:
        rest_time = car[1] - basic_time
        cost = basic_fee
        if rest_time > 0:
            k = rest_time // unit_time
            rest_time -= unit_time * k
            cost += unit_fee * k
            if rest_time > 0:
                cost += unit_fee
        res.append(cost)

    return res


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))