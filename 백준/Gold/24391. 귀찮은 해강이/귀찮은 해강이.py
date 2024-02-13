import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
group = list(range(N + 1))

def find(child):
    if group[child] != child:
        group[child] = find(group[child])
    return group[child]

def union(a, b):
    A = find(a)
    B = find(b)

    group[B] = A

for _ in range(M):
    a, b = list(map(int, input().split()))
    union(a, b)

codes = list(map(int, input().split()))

count = 0
for idx in range(len(codes) - 1):
    if find(codes[idx]) != find(codes[idx + 1]):
        count += 1

print(count)