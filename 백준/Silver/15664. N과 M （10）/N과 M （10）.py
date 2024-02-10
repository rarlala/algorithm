N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
sel = [0 for _ in range(M)]

results = []

def combi(idx, sidx):
    if sidx == M:
        result = " ".join(sel)
        if result not in results:
            results.append(result)
            print(result)
        return

    if idx == N:
        return

    sel[sidx] = str(arr[idx])

    combi(idx + 1, sidx + 1)
    combi(idx + 1, sidx)



combi(0, 0)