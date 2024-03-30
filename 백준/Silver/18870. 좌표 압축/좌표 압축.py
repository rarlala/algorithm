import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sortedArr = sorted(set(arr))
indexMap = {value: idx for idx, value in enumerate(sortedArr)}
results = []

for value in arr:
    results.append(indexMap[value])

print(*results)