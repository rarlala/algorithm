import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
arr = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            arr[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

results = [0] * n
for i in range(1, n + 1):
    sum = 0
    for j in range(1, n + 1):
        sum += arr[i][j]
    results[i - 1] = sum

print(results.index(min(results)) + 1)