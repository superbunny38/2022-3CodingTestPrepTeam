globalCnt = int(1e9)

def main():
    n = int(input())
    # count = dp(n)
    count = dfs(n, 0)
    print(count)
    
def dp(n) -> int:
    # 1 <= n <= 10**6
    
    dp = [int(1e7) for _ in range(n + 1)] # index => 1로 갈 수 있는 최소 연산 수
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
         
    return dp[n]

def dfs(n, cnt) -> int:
    global globalCnt
    
    if cnt >= globalCnt:
        return
    
    if n == 1:
        globalCnt = min(globalCnt, cnt)
        return globalCnt
    
    if n % 3 == 0:
        dfs(n // 3, cnt + 1)
    if n % 2 == 0:
        dfs(n // 2, cnt + 1)
    dfs(n - 1, cnt + 1)

    return globalCnt
    
main()