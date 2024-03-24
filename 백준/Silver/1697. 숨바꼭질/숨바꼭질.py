from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * 100001

def bfs(a):
    queue = deque([a])
    visited[a] = 1

    while queue:
        s = queue.popleft()

        if s == k:
            return print(visited[s] - 1)

        for next_s in (s * 2, s + 1, s - 1):
            if 0 <= next_s <= 100000 and not visited[next_s]:
                visited[next_s] = visited[s] + 1
                queue.append(next_s)

bfs(n)