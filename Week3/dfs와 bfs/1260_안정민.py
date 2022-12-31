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
        
        '''
        첫 풀이는 바로 ac을 받아서 아래와 같은 코드로 다시 채점을 했는데 실패
        [check(x) for x in sorted(filter(lambda x: not visited[x], graph[curr]))]
        
        - 문제점 -
        4 3 1
        1 2
        1 2
        3 4
     
        답: 1 2
        위 코드: 1 2 2
        
        실제로는 노드 중복이 있을 수 있기 때문에 for문을 돌 때마다 해당 노드가 방문했는 지를 체크해야 함
        
        운이 좋게도 filter는 generator를 반환하는데, 이는 한번에 list를 반환하는게 아닌 접근?을 할 때마다 생성을 해주어
        방문체크가 되었던 것
        
        조건(중복 간선)을 체크 못 하고 푼 거라 사실 상 틀림... 
        '''

           
    return result

main()