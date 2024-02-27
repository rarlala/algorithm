import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
arr = [[]*N for _ in range(N + 1)]
distance = [1e9] * (N + 1)

for _ in range(M):
    _start, _end, _time = list(map(int, input().split()))
    arr[_start].append([_end, _time])

def dijkstra(s):
    heap = []
    heapq.heappush(heap, (s, 0))
    distance[s] = 0

    while heap:
        g, t = heapq.heappop(heap)

        if distance[g] < t:
            continue

        for i in arr[g]:
            [e, v] = i

            if t + v < distance[e]:
                distance[e] = t + v
                heapq.heappush(heap, (e, t + v))

total = []
for j in range(1, N + 1):
    dijkstra(j)
    total.append(distance)
    distance = [1e9] * (N + 1)

result = 0
for i in range(0, N):
    result = max(result, total[i][X] +  total[X-1][i + 1])

print(result)