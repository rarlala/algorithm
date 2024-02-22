import sys
input = sys.stdin.readline

a = int(input())
b = list(input().rstrip())
b.reverse()

total = []
for i in range(len(b)):
    result = a * int(b[i])
    total.append(result * 10**i)
    print(result)

print(sum(total))