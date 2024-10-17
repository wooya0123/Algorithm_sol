def convert_sharp(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    return melody

def solution(m, musicinfos):
    m = convert_sharp(m)
    res = []

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        start_time = musicinfo[0]
        start_hour = int(start_time[:2])
        start_minute = int(start_time[3:])
        end_time = musicinfo[1]
        end_hour = int(end_time[:2])
        end_minute = int(end_time[3:])

        play_hour = end_hour - start_hour
        play_minute = end_minute - start_minute
        play_time = play_hour * 60 + play_minute

        melody = convert_sharp(musicinfo[3])
        if len(melody) > play_time:
            play_melody = melody[:play_time]
        elif len(melody) == play_time:
            play_melody = melody
        else:
            k = play_time // len(melody)
            play_melody = ''
            play_melody += (melody * k)

            rest_melody = play_time % len(melody)
            for i in range(rest_melody):
                play_melody += melody[i]

        for j in range(len(play_melody)):
            if play_melody[j] == m[0]:
                if play_melody[j:j+len(m)] == m:
                    if play_melody[j+len(m)] != '#':
                        res.append((musicinfo[2], play_time))
                        break

    if not res:
        return 'None'
    else:
        max_play_time = 0
        answer = ''
        for x in res:
            if max_play_time < x[1]:
                max_play_time = x[1]
                answer = x[0]
            elif max_play_time == x[1]:
                pass
        return answer

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))