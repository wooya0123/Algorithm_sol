N = int(input())
arr = [int(input()) for _ in range(N)]
heap = [0] * (N+1)
last = 0

for n in arr:
    if n == 0:
        if last == 0:
            print(0)
        else:
            tmp = heap[1]           # 루트값 저장
            heap[1] = heap[last]    # 맨 마지막 값을 루트로 배치
            last -= 1
            parent = 1
            child = parent * 2
            while child <= last:
                if child+1 <= last and heap[child] > heap[child+1]:     # 맨 마지막 값이 있는지 확인, 왼-오 값 중 작은 값으로
                    child += 1
                if heap[parent] > heap[child]:                          # 작은 값을 부모로
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
        while parent >= 1 and heap[parent] > heap[child]:           # 부모가 루트가 될 때까지 비교
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2



input = '''
9
0
12345678
1
2
0
0
0
0
32
'''

output = '''
0
1
2
12345678
0
'''