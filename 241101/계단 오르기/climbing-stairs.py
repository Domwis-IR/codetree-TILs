n = int(input())

def up(n):
    dp = [0] * 1001
    dp[0] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[n]

print(up(n) % 10007)