import sys
input = sys.stdin.readline
result = []

def repeat(a, b, c):
    if a == b:
        result.append(c)
    elif a > b:
        return

    repeat(a * 2, b + 3, c + 1)
    repeat(a + 1, b, c + 1)

for _ in range(int(input())):
    S, T = map(int, input().split())

    result = []
    repeat(S, T, 0)
    print(min(result))