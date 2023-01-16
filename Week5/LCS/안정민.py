def main() -> None:
    a, b = input(), input()
    maxLen = solve(a, b)
    print(maxLen)

def solve(a, b) -> int:
    aLen, bLen = len(a), len(b)
    dp = [[0] * (bLen + 1) for _ in range(aLen + 1)]
    for i in range(1, aLen + 1):
        for j in range(1, bLen + 1):
            aChar, bChar = a[i - 1], b[j - 1]
            if aChar == bChar:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

main()