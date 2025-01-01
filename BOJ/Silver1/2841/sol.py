'''
1~6번 줄, 1~p번 프랫(높은 수의 프랫의 음이 연주됨)
프랫을 누르거나 떼면 손가락 한 번 움직인 거
손가락 가장 적게 움직이는 방법
N: 음의 수, 프랫의 수: P
그 다음 N개의 줄 -> 줄 번호, 프랫 번호
주어진 순서대로 연주
'''
import sys

N, P = list(map(int, sys.stdin.readline().rstrip().split()))
melody = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

guitar = [[] for i in range(N+1)]     # 1~N번 줄
cnt = 0

for sound in melody:
    string = sound[0]
    fret = sound[1]
    # 기타 줄에 프랫이 눌러져 있으면
    if guitar[string]:
        # 눌러야 하는 프렛이 눌러져 있는 프렛보다 크면 추가
        if guitar[string][-1] < fret:
            guitar[string].append(fret)
            cnt += 1
        # 같으면 그냥 넘어감
        elif guitar[string][-1] == fret:
            continue
        # 작으면 눌러져 있는 프렛 하나씩 빼기
        else:
            while True:
                if not guitar[string] or guitar[string][-1] < fret:
                    guitar[string].append(fret)
                    cnt += 1
                    break
                elif guitar[string][-1] > fret:
                    guitar[string].pop()
                    cnt += 1
                    continue
                elif guitar[string][-1] == fret:
                    break


    # 기타 줄에 프랫이 안 눌러져 있으면
    else:
        guitar[string].append(fret)
        cnt += 1

print(cnt)