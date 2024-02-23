import heapq
import sys
input = sys.stdin.readline

city = int(input())
bus = int(input())
INF = 1e8

city_map = [[]*city for _ in range(city + 1)]
visited = [False] * (city + 1)
distance = [INF] * (city + 1)

for _ in range(bus):
    _start, _end, _cost = map(int, input().split())
    city_map[_start].append((_end, _cost))

start, end = map(int, input().split())
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if distance[now] < cost:
            continue

        for i in city_map[now]:
            if cost + i[1] < distance[i[0]]:
                distance[i[0]] = cost + i[1]
                heapq.heappush(heap, (cost + i[1], i[0]))

dijkstra(start)
print(distance[end])