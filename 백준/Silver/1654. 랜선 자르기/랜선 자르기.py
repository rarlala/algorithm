N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
left = 1
right = arr[-1]

while left <= right:
    mid = (left + right) // 2

    count = 0
    for rope in arr:
        count += rope // mid

    if count >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)