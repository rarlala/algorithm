import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    arr = [[i for i in (range(n + 1))] for _ in range(k)]

    for i in range(0, k):
        for j in range(1, n + 1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[k-1][n])
