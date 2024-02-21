import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

concents = [0] * M

i = 0
while len(arr):
    if i == 0:
        concents[0] += arr.pop()
        i = (i + 1) % M
    else:
        while concents[0] > concents[i] and arr:
            concents[i] += arr.pop()
        i = (i + 1) % M

print(concents[0])