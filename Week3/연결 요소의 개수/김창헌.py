import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
      
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1) 
cnt = 0

for i in range(1, N+1):
  if visited[i] == False:
    dfs(i)
    cnt += 1

print(cnt)