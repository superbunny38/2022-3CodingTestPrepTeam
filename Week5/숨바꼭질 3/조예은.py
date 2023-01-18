# 다익스트라 코드 검색해서 복붙함, 시간 오래 걸림 (그래프로 하면 더 짧게 걸리는듯)
import sys
import heapq


input = sys.stdin.readline
n , k = map(int, input().split())
graph = [[] for i in range(100001)]
graph[0] = [(1, 1)]
distance = [100001] * 100001

for i in range(100001):
    if i > 0:
        graph[i].append((i-1, 1))
    if i < 100000:
        graph[i].append((i+1, 1))
    if 2 * i <= 100000:
        graph[i].append((2*i, 0))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue               # 따라서 다음으로 넘어간다.

        for i in graph[now]:     # 연결된 모든 노드 탐색
            if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist+i[1]   #
                heapq.heappush(q, (dist+i[1], i[0]))


dijkstra(n)
print(distance[k])