import sys
input = sys.stdin.readline
N, K = map(int, input().split())
plusArr = []
minusArr = []

for _ in range(N):
    a, b = map(int, input().split())
    if a - b >= 0:
        plusArr.append(a-b)
    else:
        minusArr.append(a-b)

count = len(plusArr)
minusArr.sort(reverse=True)

if count >= K:
    print(0)
else:
    print(minusArr[K - count - 1] * -1)