import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solve(src, dst, graph) -> int:
    distance = [INF] * (dst + 1)
    distance[src] = 0
    hq = []
    heapq.heappush(hq, (0, src))
    while hq:
        dist, curr = heapq.heappop(hq)
        if dist > distance[curr]:
            continue
        for cost, next in graph[curr]:
            newDist = dist + cost
            if newDist < distance[next]:
                distance[next] = newDist
                heapq.heappush(hq, (newDist, next))
    
    return distance[dst]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
    graph[e].append((c, s))
    
print(solve(1, n, graph))