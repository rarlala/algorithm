N = int(input())
arr = []

for _ in range(N):
    age, name = list(input().split())
    arr.append((int(age), name))

arr = sorted(arr, key=lambda x: (x[0]))

for data in arr:
    print(f"{data[0]} {data[1]}")