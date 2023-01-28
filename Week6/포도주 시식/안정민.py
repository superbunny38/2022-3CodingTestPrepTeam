import sys
input = sys.stdin.readline

def main():
    n = int(input())
    drinks = [int(input()) for _ in range(n)]
    maxV = solve(n, drinks)
    print(maxV)

def solve(n, drinks):
    dp = [[] for _ in range(n + 1)]
    dp[1] = [(0, 0), (1, drinks[0])]
    for i in range(1, n + 1):
        now = drinks[i - 1]
        maxPrev = 0
        for cnt, prev in dp[i - 1]:
            maxPrev = max(maxPrev, prev)
            if cnt == 2:
                continue
            dp[i].append((cnt + 1, prev + now))
        dp[i].append((0, maxPrev))
        
    return max(dp[n], key = lambda x: x[1])[1]

main()
