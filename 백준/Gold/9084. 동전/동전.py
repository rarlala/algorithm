T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    C = int(input())
    dp = [0] * (C + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, C + 1):
            dp[i] += dp[i-coin]

    print(dp[C])