from collections import deque
# n: 정점의 개수, m: 간선의 개수, v:탐색을 시작할 정점의 번호
n, m, v = map(int,input().split())
 
graph = [[] for _ in range(n+1)]
 
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for j in graph[v]:
        if not visited[j]:
            dfs(graph, j, visited)
 
# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True
                
visited = [False] * (n+1)        
dfs(graph, v, visited)
print("")
visited = [False] * (n+1)
bfs(graph, v, visited)