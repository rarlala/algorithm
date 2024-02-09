from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ripe_tomato = set()
queue = deque()
tomato_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ripe_tomato.add((i, j))
            queue.append((i, j, 0))
            tomato_cnt += 1
        elif arr[i][j] == 0:
            tomato_cnt += 1

while queue:
    r, c, date = queue.popleft()

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in ripe_tomato and arr[nr][nc] == 0 :
            ripe_tomato.add((nr, nc))
            queue.append((nr, nc, date + 1))

if tomato_cnt == len(ripe_tomato):
    print(date)
else:
    print(-1)