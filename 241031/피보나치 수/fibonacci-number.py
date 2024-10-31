# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

def fibo(n):
    if dp[n] != -1:
        return dp[n]
    if n <= 2:
        dp[n] = 1
    else:
        dp[n] = dp[n-2] + dp[n-1]
    
    return dp[n]

n = int(input())
dp = [-1] * (n+1)
print(fibo(n))