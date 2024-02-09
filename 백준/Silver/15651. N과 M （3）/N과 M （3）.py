N, M = list(map(int, input().split()))

arr = [i + 1 for i in range(N)]
sel = [0 for _ in range(M)]
choice = [0 for _ in range(N)]

def perm(depth):
    if depth == M:
        print(" ".join(sel))
        return

    for i in range(N):
        sel[depth] = str(arr[i])
        perm(depth + 1)

perm(0)