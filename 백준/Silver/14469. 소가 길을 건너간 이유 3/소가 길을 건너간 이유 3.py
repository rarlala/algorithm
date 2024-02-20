N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

time = 0
for cow in arr:
    if time < cow[0]:
        time = cow[0]
    time += cow[1]

print(time)