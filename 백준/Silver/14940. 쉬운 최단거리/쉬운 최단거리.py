# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# result_arr = [[-1] * m for _ in range(n)]
#
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     result_arr[x][y] = 0
#
#     while queue:
#         a, b = queue.popleft()
#
#         for i in range(4):
#             na = a + dr[i]
#             nb = b + dc[i]
#
#             if 0 <= na < n and 0 <= nb < m and arr[na][nb] == 1 and result_arr[na][nb] == -1:
#                 result_arr[na][nb] = result_arr[a][b] + 1
#                 queue.append((na, nb))
#
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 2:
#             bfs(i, j)
#
# for i in result_arr:
#     print(*i)

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result_arr = [[-1] * m for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    result_arr[x][y] = 0

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            na = a + dr[i]
            nb = b + dc[i]

            if 0 <= na < n and 0 <= nb < m and arr[na][nb] == 1 and result_arr[na][nb] == -1:
                result_arr[na][nb] = result_arr[a][b] + 1
                queue.append((na, nb))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            result_arr[i][j] = 0
            bfs(i, j)
        elif arr[i][j] == 0:
            result_arr[i][j] = 0

for i in result_arr:
    print(*i)
