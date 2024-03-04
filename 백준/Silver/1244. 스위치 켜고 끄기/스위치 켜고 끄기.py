import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
for _ in range(int(input())):
    g, n = map(int, input().split())
    if g == 1:
        for i in range(n - 1, len(arr), n):
            arr[i] = 0 if arr[i] else 1
    else:
        idx = n - 1
        count = 1
        while 0 <= idx - count and idx + count < len(arr) and arr[idx - count] == arr[idx + count]:
            count += 1
        count -= 1
        for i in range(idx - count, idx + count + 1):
            arr[i] = 0 if arr[i] else 1

for i in range(0, len(arr), 20):
    print(*arr[i:i+20])