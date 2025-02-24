from heapq import heappush, heappop

N = int(input())
arr = [int(input()) for _ in range(N)]

# 기본값이 최소힙 -> 값을 넣을 때 -를 붙여서 넣고 뺄 때 다시 -붙여서 빼기
heap = []

for n in arr:
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -n)
