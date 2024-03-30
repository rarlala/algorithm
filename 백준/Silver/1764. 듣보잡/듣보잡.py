import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = set([input().rstrip() for _ in range(n)])
arr2 = set([input().rstrip() for _ in range(m)])
results = arr1 & arr2
results = sorted(list(results))
print(len(results))
for people in results:
    print(people)