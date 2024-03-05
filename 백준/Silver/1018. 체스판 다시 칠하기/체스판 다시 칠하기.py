N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
counts = []

def check(r, c, startColor):
    count = 0

    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if (i - r) % 2 == 0 and (j - c) % 2 == 0:
                if arr[i][j] != startColor:
                    count += 1
            elif (i - r) % 2 == 1 and (j - c) % 2 == 1:
                if arr[i][j] != startColor:
                    count += 1
            else:
                if arr[i][j] == startColor:
                    count += 1
    counts.append(count)


for n in range(0, N-7):
    for m in range(0, M-7):
        check(n, m, "W")
        check(n, m, "B")

print(min(counts))