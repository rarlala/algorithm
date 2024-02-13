n, m = list(map(int, input().split()))
group = [i for i in range(n+1)]

def find(child):
    if child != group[child]:
        group[child] = find(group[child])
    return group[child]

def union(a, b):
    A = find(a)
    B = find(b)

    group[B] = A

for _ in range(m):
    i, a, b = list(map(int, input().split()))

    if i == 1:
        A = find(a)
        B = find(b)
        print("yes" if A == B else "no")
    else:
        union(a, b)