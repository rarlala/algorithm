import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
arr = [[] for _ in range(4)]
result = True

for a in A:
    for i in range(4):
        if len(arr[i]) == 0:
            arr[i].append(a)
            break
        elif arr[i][-1] < a:
            arr[i].append(a)
            break

for n in range(N, 0, -1):
    for j in range(4):
        if len(arr[j]) > 0 and arr[j][-1] == n:
            arr[j].pop()
            break
    else:
        result = False

print("YES" if result else "NO")