import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
newArr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    heap = []
    heapq.heappush(heap, (x, y))

    while heap:
        a, b = heapq.heappop(heap)

        ice = 0
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    ice += 1
                if not visited[nx][ny] and arr[nx][ny] != 0:
                    heapq.heappush(heap, (nx, ny))
                    visited[nx][ny] = 1

        newArr[a][b] = 0 if arr[a][b] - ice < 0 else arr[a][b] - ice

year = 0
while True:
    newArr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0
    zero = True

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                zero = False
                if not visited[i][j]:
                    bfs(i, j)
                    count += 1

    if count >= 2:
        print(year)
        break
    elif zero:
        print(0)
        break

    year += 1
    arr = newArr