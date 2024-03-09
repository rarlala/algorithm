import sys
input = sys.stdin.readline
N = int(input())
dict = {}
for _ in range(N):
    file = input().strip()
    n, e = file.split(".")

    if e in dict:
        dict[e] = dict[e] + 1
    else:
        dict[e] = 1

sorted_dict = sorted(dict.items())
for d in sorted_dict:
    print(*d)