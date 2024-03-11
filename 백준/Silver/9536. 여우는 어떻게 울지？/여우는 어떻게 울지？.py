import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(input().split())

    while True:
        value = input().rstrip()
        if value == "what does the fox say?":
            print(*arr)
            break

        a, b, c = list(value.split())
        newArr = []
        for data in arr:
            if data != c:
                newArr.append(data)
        arr = newArr