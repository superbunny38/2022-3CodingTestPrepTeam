def main():
    n = int(input())
    result = fibonacci(n)
    print(result)
    
def fibonacci(n) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

main()