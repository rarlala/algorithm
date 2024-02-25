import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
count = [0 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        s = q.popleft()
        if s == G:
            return count[s]
        for i in (s+U, s-D):
            if 1 <= i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[s] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"

print(bfs(S))