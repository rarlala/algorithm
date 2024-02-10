N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
sel = [0 for _ in range(M)]

results = []

def perm(depth):
    if depth == M:
        result = " ".join(sel)
        if result not in results:
            results.append(result)
            print(result)
        return

    for i in range(N):
        if depth == 0 or (depth > 0 and arr[i] >= int(sel[depth - 1])):
            sel[depth] = str(arr[i])
            perm(depth + 1)
            continue


perm(0)
