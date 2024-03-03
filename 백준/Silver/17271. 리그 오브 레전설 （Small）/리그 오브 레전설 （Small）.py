import sys

N, M = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in range(1, N+1):
    dp[i] = dp[i-1]
    if i >= M:
        dp[i] = (dp[i] + dp[i-M]) % 1_000_000_007

print(dp[N])