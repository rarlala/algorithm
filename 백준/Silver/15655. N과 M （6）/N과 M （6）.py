N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

sel = [0 for _ in range(M)]

def combi(idx, sidx):
    if sidx == M:
        print(" ".join(sel))
        return

    if idx == N:
        return

    sel[sidx] = str(arr[idx])
    combi(idx + 1, sidx + 1)
    combi(idx + 1, sidx)


combi(0, 0)