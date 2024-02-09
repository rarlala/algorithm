N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

sel = [0 for _ in range(M)]
choice = [0 for _ in range(N)]

def perm(depth):
    if depth == M:
        print(" ".join(sel))
        return

    for i in range(N):
        if not choice[i]:
            choice[i] = 1
            sel[depth] = str(arr[i])
            perm(depth + 1)
            choice[i] = 0


perm(0)