from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    name, count = input().split()
    queue.append((name, count))

while queue:
    name, count = queue.popleft()

    if len(queue) <= 1:
        print(name)
        break
    else:
        for _ in range(int(count) - 1):
            queue.append(queue.popleft())
        queue.popleft()
