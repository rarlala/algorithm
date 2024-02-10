N, M = list(map(int, input().split()))
data = {}

for _ in range(N):
    site, password = list(input().split())
    data[site] = password

for _ in range(M):
    site = input()
    print(data[site])
