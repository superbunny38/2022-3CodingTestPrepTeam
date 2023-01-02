totalCnt = 0

def main():
    global totalCnt
    
    t = int(input())
    
    for _ in range(t):
        dfs(0, int(input()))
        print(totalCnt)
        totalCnt = 0

def dfs(now, n) -> int:
    global totalCnt
    
    if now >= n:
        totalCnt += (1 if now == n else 0)
        return totalCnt
    
    dfs(now + 1, n)
    dfs(now + 2, n)
    dfs(now + 3, n)
    
    return totalCnt

main()