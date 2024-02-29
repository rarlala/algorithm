from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
result = [0 for _ in range(N)]
count = 1

def bfs(s):
    global count
    q = deque()
    q.append(s)

    while q:
        a = q.popleft()

        data = sorted(arr[a])
        for i in range(len(data)):
            if not result[data[i] - 1]:
                count += 1
                result[data[i] - 1] = count
                q.append(data[i])

for _ in range(M):
    u, v = list(map(int, input().split()))
    arr[u].append(v)
    arr[v].append(u)

result[R-1] = 1
bfs(R)

for i in result:
    print(i)