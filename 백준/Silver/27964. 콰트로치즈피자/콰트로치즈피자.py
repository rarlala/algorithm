import sys
input = sys.stdin.readline
N = int(input())
arr = list(set(list(input().split())))
count = 0
for topping in arr:
    if topping.endswith("Cheese"):
        count += 1
print("yummy" if count >= 4 else "sad")