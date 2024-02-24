import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
arr = [[] * (V + 1) for _ in range(V+1)]
INF = 1e9
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    arr[u].append((v, w))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        value, now = heapq.heappop(heap)

        if distance[now] < value:
            continue

        for i in arr[now]:
            end = i[0]
            cost = i[1]

            if value + cost < distance[end]:
                distance[end] = value + cost
                heapq.heappush(heap, (value + cost, end))

dijkstra(K)
distance.pop(0)

for num in distance:
    print("INF" if num == 1e9 else num)