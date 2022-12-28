from collections import deque

def bfs(graph, v, visited):
  q = deque([v])
  visited[v] = True
  while q:
    u = q.popleft()
    for k in graph[u]:
      if not visited[k]:
        q.append(k)
        visited[k] =  True
        
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1) 
cnt = 0

for i in range(1, N+1):
  if visited[i]: continue
  bfs(graph, i, visited)
  cnt += 1

print(cnt)