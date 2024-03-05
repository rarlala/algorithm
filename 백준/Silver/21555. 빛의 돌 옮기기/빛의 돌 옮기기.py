import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0]*2 for _ in range(N)]
dp[0][0], dp[0][1] = A[0], B[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0] + A[i], dp[i-1][1] + A[i] + K)
    dp[i][1] = min(dp[i-1][0] + B[i] + K, dp[i-1][1] + B[i])

print(min(dp[N-1]))