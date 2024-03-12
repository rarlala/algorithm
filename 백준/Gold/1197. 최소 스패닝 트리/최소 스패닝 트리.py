import sys
input = sys.stdin.readline
V, E = map(int, input().split())
arr = [i for i in range(V+1)]
edges = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        arr[B] = A
    else:
        arr[A] = B

total_cost = 0
for edge in edges:
    x, y, cost = edge

    if find(x) != find(y):
        union(x, y)
        total_cost += cost

print(total_cost)