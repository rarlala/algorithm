import sys
input = sys.stdin.readline

n = int(input())
cards = sorted([*map(int, input().split())])
m = int(input())
datas = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0
        
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in datas:
    print(binarySearch(cards, target, 0, len(cards) - 1), end=" ")