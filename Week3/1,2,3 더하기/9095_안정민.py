totalCnt = 0

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        # dfs(0, n)
        # print(totalCnt)
        # totalCnt = 0
        
        count = dp(n)
        print(count)

def dfs(now, n) -> int:
    global totalCnt
    
    if now >= n:
        totalCnt += (1 if now == n else 0)
        return totalCnt
    
    dfs(now + 1, n)
    dfs(now + 2, n)
    dfs(now + 3, n)
    
    return totalCnt

def dp(n) -> int: 
    # 1 2 4 7 13
    # 1 -> 1
    # 2 -> 1 1 // 2
    # 3 -> 1 1 1 // 2 1 / 1 2 // 3
    # 4 -> 1 1 1 1 // 2 1 1 / 1 2 1 / 1 1 2 / 2 2 // 3 1 / 1 3
    # 5 -> 1 1 1 1 1 // 2 1 1 1 / 1 2 1 1 / 1 1 2 1 / 1 1 1 2 / 2 2 1 / 2 1 2 / 1 2 2 // 3 1 1 / 1 3 1 / 1 1 3 / 2 3 / 3 2
    
    '''
    dp로 풀려고 했는데 너무 생각이 안나서 예전에 풀었던 것 확인...
    자기 자신에서 -1, -2, -3 의 방법 수에 1, 2, 3을 추가하여 이런저런 조합을 하면 될 것 같았는데, 
    각각에서 중복이 나오는 것을 어떻게 처리해야 할 지 생각이 안 남
    
    결론은 1 + (i-1), 2 + (i-2), 3 + (i-3) 처럼 중복을 생각할 것 없이, 
    1+로 시작하는 경우, 2+로 시작하는 경우, 3+로 시작하는 경우를 다 더하면 됨!
    '''
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for i in range(1, n + 1):
        for j in [1, 2, 3]:
            ways[i] += (ways[i - j] if i >= j else 0)
    
    return ways[n]

main()