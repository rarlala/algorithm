import sys
input = sys.stdin.readline

N = int(input())
heap = []

def heap_push(item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    while heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def heap_pop():
    if len(heap) == 0:
        print(0)
        return

    result = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    parent = 0
    child = parent * 2

    if child + 1 <= len(heap) - 1:
        if heap[child] > heap[child + 1]:
            child += 1

    while child <= len(heap) - 1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    print(result)

for _ in range(N):
    number = int(input())

    if number == 0:
        heap_pop()
    else:
        heap_push(number)