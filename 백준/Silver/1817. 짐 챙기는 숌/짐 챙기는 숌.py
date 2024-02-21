import sys
input = sys.stdin.readline
N, M = map(int, input().split())
books = [] if N == 0 else list(map(int, input().split()))

count = 0
weight = 0
for book in books:
    if weight + book > M:
        count += 1
        weight = book
    elif weight + book == M:
        count += 1
        weight = 0
    else:
        weight += book

if weight != 0:
    count += 1

print(count)