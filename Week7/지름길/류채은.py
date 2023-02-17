#1446_지름길_다익스트라_silver1
#가져온 풀이: https://jie0025.tistory.com/200
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

#일단 거리 1로 초기화.
for i in range(d):
    graph[i].append((i+1, 1))

#지름길 있는 경우에 업데이트
for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d:# 고려 안해도 됨.
        continue
    graph[s].append((e,l))

dijkstra(0)
print(distance[d])
