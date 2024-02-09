N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
choice = [0 for i in range(N)]

results = []
sel = [0 for _ in range(M)]

def perm(depth):
    if depth == M:
        result = " ".join(sel)

        if result not in results:
            results.append(result)
            print(result)
        return

    for i in range(N):
        if not choice[i]:
            choice[i] = 1
            sel[depth] = str(arr[i])
            perm(depth + 1)
            choice[i] = 0

perm(0)