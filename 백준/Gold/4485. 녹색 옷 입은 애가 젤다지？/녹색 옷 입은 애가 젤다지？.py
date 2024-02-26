import heapq
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
while True:
    T = int(input())
    count += 1

    if T == 0:
        break

    INF = 1e9
    distance = [[INF] * T for _ in range(T)]
    arr = [list(map(int, input().split())) for _ in range(T)]

    heap = []
    heapq.heappush(heap, (0, 0, arr[0][0]))
    distance[0][0] = arr[0][0]

    while heap:
        x, y, value = heapq.heappop(heap)

        if distance[x][y] < value:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < T and 0 <= ny < T:
                if distance[nx][ny] > value + arr[nx][ny]:
                    distance[nx][ny] = value + arr[nx][ny]
                    heapq.heappush(heap, (nx, ny, value + arr[nx][ny]))

    print(f"Problem {count}: {distance[T-1][T-1]}")