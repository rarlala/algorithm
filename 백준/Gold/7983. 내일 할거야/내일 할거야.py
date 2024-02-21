import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]), reverse=True)

start = arr[0][1]

for i in range(n):
    s = arr[i][0]
    e = arr[i][1]

    if start >= e:
        start = e - s
    else:
        start = start - s

print(start)