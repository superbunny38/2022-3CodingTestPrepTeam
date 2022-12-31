from collections import deque

def main() -> None:
    n, m, start = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    dfsPath: list[int] = dfs(start, graph, n)
    bfsPath: list[int] = bfs(start, graph, n)
    print(' '.join(map(str, dfsPath)))
    print(' '.join(map(str, bfsPath)))
    return
    
def dfs(start, graph, maxV) -> list:
    def check(x):
        visited[x] = True
        stack.append(x)
        result.append(x)
        
    result = []
    visited = [False for _ in range(maxV + 1)]
    
    stack = deque()
    check(start)
    
    while stack:
        curr = stack[-1]
        
        targetList: list[int] = list(filter(lambda x: not visited[x], graph[curr]))
        if not targetList:
            stack.pop()
            continue
        
        next = sorted(targetList)[0]
        check(next)
    
    return result

def bfs(start, graph, maxV) -> list:
    def check(x):
        visited[x] = True
        dq.append(x)
    
    result = []
    visited = [False for _ in range(maxV + 1)]
    dq = deque()
    check(start)

    while dq:
        curr = dq.popleft()
        result.append(curr)
        
        [check(x) for x in filter(lambda x: not visited[x], sorted(graph[curr]))]
           
    return result

main()