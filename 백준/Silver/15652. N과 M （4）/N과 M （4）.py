N, M = list(map(int, input().split()))

arr = [i + 1 for i in range(N)]
sel = [0 for _ in range(M)]
results = []

def perm(depth):
    if depth == M:
        result = " ".join(sel)

        if result not in results:
            results.append(" ".join(sel))
            print(" ".join(sel))
        return

    for i in range(N):
        if depth == 0 or int(sel[depth - 1]) <= arr[i]:
            sel[depth] = str(arr[i])
            perm(depth + 1)

perm(0)