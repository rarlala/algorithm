N, M = list(map(int, input().split()))
times = sorted(list(map(int, input().split())))

left = 0
right = times[-1] * M

while left <= right:
    mid = (left + right) // 2
    balloons = sum(mid // time for time in times)

    if balloons >= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)