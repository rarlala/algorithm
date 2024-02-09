N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

sel = [0 for _ in range(M)]

def perm(depth):
    if depth == M:
        print(" ".join(sel))
        return

    for i in range(N):
        sel[depth] = str(arr[i])
        perm(depth + 1)

perm(0)