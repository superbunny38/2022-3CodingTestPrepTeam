def main() -> None:
    n = int(input())
    seq = list(map(int, input().split()))
    
    length = solve(n, seq)
    print(length)

def solve(n, seq) -> int:
    
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n + 1):
        now = seq[i - 1]
        for j in range(0, i):
            comp = seq[j - 1]
            if compare(now, comp):
                dp[i] = max(dp[i], dp[j] + 1)
                
        if dp[i] == 0:
            dp[i] = 1
    
    return max(dp)

def compare(x, y) -> bool:
    return x < y

main()