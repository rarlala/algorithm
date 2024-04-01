import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h_arr = list(map(int, input().split()))
arr = [0] * (n + 1)

for _ in range(m):
    a, b, k = map(int, input().split())
    arr[a - 1] += k
    arr[b] -= k

for i in range(1, n):
    arr[i] += arr[i - 1]

for i in range(n):
    h_arr[i] += arr[i]

print(*h_arr)
