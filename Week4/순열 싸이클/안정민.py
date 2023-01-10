import sys
sys.setrecursionlimit(int(1e5))

def main() -> None:
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        numberList = list(map(int, input().split()))
        cnt = solve(n, numberList)
        print(cnt)
        
def solve(n, numberList) -> int:
    visited = [False] * (n + 1)
    
    cycleCnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        dfs(i, numberList, visited)
        cycleCnt += 1
        
    return cycleCnt

def dfs(start, nodeList, visited) -> None:
    next = nodeList[start - 1]
    if visited[next]:
        return
    
    visited[next] = True
    dfs(next, nodeList, visited)

main()