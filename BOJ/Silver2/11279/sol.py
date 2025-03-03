# 최대힙
# 숫자 -> 숫자를 배열에 추가
# 0 -> 가장 큰 값을 출력 후 그 값을 배열에서 제거
# 배열에서 제거된 횟수만큼 답 출력 - 배열이 비었는데 출력한 경우 0출력


N = int(input())
arr = [int(input()) for _ in range(N)]

heap = [0] * (N+1)
last = 0

for n in arr:
    if n == 0:
        if last == 0:       # 배열이 비었는데 빼라고 하면 0출력
            print(0)
        else:
            tmp = heap[1]      # 루트값 저장
            heap[1] = heap[last]  # 맨 마지막 값을 루트로 가져오기
            last -= 1
            parent = 1
            child = parent * 2
            while child <= last:    # 루트부터 자식이랑 값 비교
                if child+1 <= last and heap[child] < heap[child+1]:   # 오른쪽 자식이 있는지 확인, 있으며 왼-오 값 비교
                    child += 1
                if heap[parent] < heap[child]:                        # 부모와 자식 값 비교, 큰 값을 부모로
                    heap[parent], heap[child] = heap[child], heap[parent]
                    parent = child
                    child = parent * 2
                else:
                    break
            print(tmp)
    else:
        last += 1
        heap[last] = n
        child = last
        parent = child // 2
        while parent >= 1 and heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2


input = '''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''

output = '''
0
2
1
3
2
1
0
0
'''