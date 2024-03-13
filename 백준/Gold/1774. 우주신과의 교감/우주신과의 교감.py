import math
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(N + 1)]

def find(a):
    if arr[a] != a:
        arr[a] = find(arr[a])
    return arr[a]

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        arr[B] = A
    else:
        arr[A] = B

gods = []
for _ in range(N):
    x, y = map(int, input().split())
    gods.append((x, y))

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

result = 0
costs = []
for i in range(0, N):
    for j in range(i + 1, N):
        cost = math.sqrt((gods[i][0] - gods[j][0]) ** 2 + (gods[i][1] - gods[j][1]) ** 2)
        costs.append((cost, i, j))

costs.sort(key=lambda x:x[0])
for c in costs:
    cost, a, b = c

    if find(a+1) != find(b+1):
        union(a+1, b+1)
        result += cost

print(f"{result:.2f}")