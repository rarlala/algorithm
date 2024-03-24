import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
queue = deque()
def deque(a, b):
    if a == "push_front":
        queue.appendleft(b)
    elif a == "push_back":
        queue.append(b)
    elif a == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif a == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif a == "size":
        print(len(queue))
    elif a == "empty":
        print(1 if len(queue) == 0 else 0)
    elif a == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif a == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

for _ in range(t):
    data = input()

    if len(data.split()) > 1:
        a, b = data.split()
        deque(a.rstrip(), int(b))
    else:
        deque(data.rstrip(), 0)
