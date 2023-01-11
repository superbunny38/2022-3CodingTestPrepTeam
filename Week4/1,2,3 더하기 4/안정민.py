def main() -> None:
    t = int(input())
    for _ in range(t):    
        n = int(input())
        cnt = solve(n)
        print(cnt)

def solve(n) -> int:
    # 1 -> 1
    # 2 -> 1 1 // 2
    # 3 -> 1 1 1 // 1 2 // 3
    # 4 -> 1 1 1 1 // 1 1 2 / 2 2 // 1 3 
    # 5 -> 1 1 1 1 1 // 1 1 1 2 / 1 2 2 // 1 1 3 / 2 3
    # 6 -> 1 1 1 1 1 1 // 1 1 1 1 2 / 1 1 2 2 / 2 2 2 // 1 1 1 3 / 1 2 3 / 3 3
    dp = [1] * (n + 1)
    for way in [2, 3]:
        for i in range(2, n + 1):
            if way <= i:
                dp[i] += dp[i - way]
                
    return dp[n]

main()