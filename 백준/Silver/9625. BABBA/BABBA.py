import sys
N = int(sys.stdin.readline())
arr = [[1,0], [0, 1]]

for i in range(2, N+1):
    x = arr[i-2][0] + arr[i-1][0]
    y = arr[i-2][1] + arr[i-1][1]
    arr.append([x, y])

print(*arr[N])