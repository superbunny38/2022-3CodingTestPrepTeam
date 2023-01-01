from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
# 입력이 최대 50만개 정도라 readline없이 pypy 환경이 아니라면 시간 초과

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    count = solve(graph)
    print(count)
        
def solve(graph) -> int:
       
    connectCnt = 0
    
    n = len(graph)
    visited = [False for _ in range(n)]
    
    for node in range(1, n):
        
        if visited[node]:
            continue
        
        dfs(node, graph, visited)
        # bfs(node, graph, visited)
        
        connectCnt += 1
        
    return connectCnt

def dfs(start, graph, visited) -> None:
    for next in graph[start]:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next, graph, visited)

def bfs(start, graph, visited) -> None:
    def check(node):
        visited[node] = True
        dq.append(node)
        
    dq: deque[int] = deque()
    check(start)
    
    while dq:
        curr = dq.popleft()
        [check(node) for node in filter(lambda x: not visited[x], graph[curr])] 

main()