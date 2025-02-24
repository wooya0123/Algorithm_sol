from heapq import heappush, heappop

N = int(input())
arr = [int(input()) for _ in range(N)]
heap = []

for n in arr:
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, n)