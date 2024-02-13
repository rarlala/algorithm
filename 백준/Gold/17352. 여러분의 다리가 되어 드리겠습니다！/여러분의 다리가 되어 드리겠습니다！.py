import sys
input = sys.stdin.readline

n = int(input())
parents = list(range(n+1))

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for _ in range(n-2):
    island1, island2 = map(int,input().split())
    union(island1, island2)

for i in range(2,n+1):
    if find(1) != find(i):
        print(1,i)
        break