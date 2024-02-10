N, M = list(map(int, input().split()))
arr = sorted(list(set(list(map(int, input().split())))))
sel = [0 for _ in range(M)]

def perm(depth):
    if depth == M:
        print(" ".join(sel))
        return

    for i in range(len(arr)):
        sel[depth] = str(arr[i])
        perm(depth + 1)


perm(0)
