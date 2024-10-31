n = int(input())

def up(n):
    dp = [0] * 1001
    dp[2] = 1
    dp[3] = 1
    dp[4] = 1
    for i in range(5, n+1):
        dp[n] = dp[n-2] + dp[n-3]
    return dp[n]

print(up(n))