# 데이터 전처리
def convert_sharp_notes(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    return melody

def solution(m, musicinfos):
    m = convert_sharp_notes(m)
    res = []

    for info in musicinfos:
        # 데이터 뽑아내서 변수에 저장
        start, end, title, melody = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        play_time = (end_h - start_h) * 60 + (end_m - start_m)

        # 재생되는 멜로디 저장
        melody = convert_sharp_notes(melody)
        play_melody = (melody * (play_time // len(melody) + 1))[:play_time]

        # 재생되는 멜로디 안에 기억한 멜로디가 있는지 확인
        for j in range(len(play_melody)):
            if play_melody[j] == m[0]:
                if play_melody[j:j + len(m)] == m:
                    res.append((title, play_time))
                    break
    if not res:
        return '(None)'
    else:
        max_play_time = 0
        answer = ''
        for x in res:
            if max_play_time < x[1]:
                max_play_time = x[1]
                answer = x[0]
        return answer


m = "CDCDF"
musicinfos = ["13:50,14:02,WORLD,CDCDCDF"]
print(solution(m, musicinfos))