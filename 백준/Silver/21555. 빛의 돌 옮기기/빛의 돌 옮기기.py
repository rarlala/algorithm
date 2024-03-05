import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

turn = 0 if A[0] < B[0] else 1
total = A[0] if A[0] < B[0] else B[0]
for i in range(1, N):
    if turn == 0:
        if A[i] > B[i] + K:
            total += B[i] + K
            turn = 1
        else:
            total += A[i]
    else:
        if B[i] > A[i] + K:
            total += A[i] + K
            turn = 1
        else:
            total += B[i]
print(total)