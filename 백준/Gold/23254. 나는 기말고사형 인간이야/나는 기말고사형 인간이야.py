import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
N *= 24

score = list(map(int, input().split()))
up_score = list(map(int, input().split()))

heap = []
for i in range(M):
    heapq.heappush(heap, [-up_score[i], score[i]])

time = 0
answer = 0
while heap and time < N:
    b, a = heapq.heappop(heap)
    if (100 - a) // -b < N - time:
        tmp = a + (-b * ((100 - a) // (-b)))
        if tmp == 100:
            answer += 100
        else:
            heapq.heappush(heap, [-(100-tmp), tmp])
        time += (100 - a) // (-b)
    else:
        answer += a + (N - time) * -b
        time += N - time

for b,a in heap:
    answer += a

print(answer)