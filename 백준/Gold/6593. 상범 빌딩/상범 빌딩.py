from collections import deque

results = []
isEnd = False
while not isEnd:
    # L: 층수, R은 행, C는 열
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        isEnd = True

    building = []
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for _ in range(L):
        arr = []
        for _ in range(R):
            arr.append(list(input()))

        input()
        building.append(arr)


    def bfs(a, b, c, count):
        Q = deque()
        Q.append((a, b, c, count))
        visited[a][b][c] = True

        global results

        while Q:
            x, y, z, count = Q.popleft()

            if building[x][y][z] == "E":
                results.append(f"Escaped in {count} minute(s).")
                return

            if x + 1 < L and not visited[x + 1][y][z] and (building[x + 1][y][z] == "." or building[x + 1][y][z] == "E"):
                Q.append((x + 1, y, z, count + 1))
                visited[x + 1][y][z] = True

            if 0 <= x - 1 and not visited[x - 1][y][z] and (building[x - 1][y][z] == "." or building[x - 1][y][z] == "E"):
                Q.append((x - 1, y, z, count + 1))
                visited[x - 1][y][z] = True

            for a in range(4):
                nr = y + dr[a]
                nc = z + dc[a]

                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[x][nr][nc] and (building[x][nr][nc] == "." or building[x][nr][nc] == "E"):
                        Q.append((x, nr, nc, count + 1))
                        visited[x][nr][nc] = True

        results.append("Trapped!")


    # 시작지점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == "S" and not visited[i][j][k]:
                    bfs(i, j, k, 0)


for result in results:
    print(result)