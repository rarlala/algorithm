r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
visited = set()
ans = 0

def dfs(x, y, count):
    global ans
    ans = max(ans, count)

    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]

        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in visited:
            visited.add(arr[nx][ny])
            dfs(nx, ny, count + 1)
            visited.remove(arr[nx][ny])

visited.add(arr[0][0])
dfs(0, 0, 1)
print(ans)