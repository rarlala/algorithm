from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

T = int(input())
count = 0

for _ in range(T):
    I = int(input())
    arr = [[0] * I for _ in range(I)]
    visited = [[0] * I for _ in range(I)]

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    arr[end[0]][end[1]] = 1

    queue = deque()
    queue.append([start[0], start[1], 0])

    while queue:
        x, y, count = queue.popleft()

        if arr[x][y] == 1:
            print(count)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                queue.append([nx, ny, count + 1])
                visited[nx][ny] = 1