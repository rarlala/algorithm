import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = map(int, input().split())
heap = []

for num in arr:
    heapq.heappush(heap, num)

for _ in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result = a + b

    heapq.heappush(heap, result)
    heapq.heappush(heap, result)

print(sum(heap))
