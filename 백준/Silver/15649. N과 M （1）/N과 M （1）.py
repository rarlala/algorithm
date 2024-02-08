N, M = list(map(int, input().split()))
results = []

arr = [i + 1 for i in range(N)]
sel = [0 for _ in range(M)]
check = [0 for _ in range(N)]


def perm(depth):
    if depth == M:
        result = " ".join(sel)
        results.append(result)
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            sel[depth] = str(arr[i])
            perm(depth + 1)
            check[i] = 0

perm(0)

for i in range(len(results)):
    print(results[i])