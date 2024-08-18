import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        max_box = max(boxes)
        min_box = min(boxes)
        for i in range(len(boxes)):
            if boxes[i] == max_box:
                boxes[i] -= 1
                break
        for j in range(len(boxes)):
            if boxes[j] == min_box:
                boxes[j] += 1
                break
    print(f'#{tc} {max(boxes) - min(boxes)}')

