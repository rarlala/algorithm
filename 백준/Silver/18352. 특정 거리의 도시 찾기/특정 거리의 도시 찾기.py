import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
INF = 1e9
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    distance[start] = 0

    while heap:
        s, c = heapq.heappop(heap)

        if distance[s] < c:
            continue

        for i in arr[s]:
            if c + 1 < distance[i]:
                distance[i] = c + 1
                heapq.heappush(heap, (i, c + 1))

dijkstra(x)

results = [i for i in range(1, n + 1) if distance[i] == k]

if not results:
    print(-1)
else:
    for result in results:
        print(result)
