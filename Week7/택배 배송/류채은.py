#지름길 풀이 응용
import heapq
import sys

######## INPUT
N,M = map(int, input().split())#N: 헛간의 개수 M: 소들의 길
#1: 현서, N: 찬홍

graph = [[] for _ in range(N+1)]
distance = [float('inf')]*(N+1)#최소 비용 담을 공간

for _ in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

#print(graph)

def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    #print(q)
    distance[start] = 0

    while q:
        cost,cur_position = heapq.heappop(q)#튜플 앞 값(cost)을 기준으로 우선순위 정해짐
        #print("visiting:",cur_position," cost:",cost," route:",visited)
        #cost: 지금 위치(cur_position)까지 올 때의 cost
        if cost>distance[cur_position]:
            #print("continue")
            #print(distance[cur_position])
            continue

        for i in graph[cur_position]:
            end_point,dist = i[0],i[1]
            if cost+dist < distance[end_point]:
                #print("end point:",end_point,"dist:",dist)
                #cost+dist: 처음부터 지금 위치까지 비용(cost)+지금위치에서 endppint까지 비용(dist)
                distance[end_point] = cost+dist#최소 비용 갱신
                heapq.heappush(q,(cost+dist,end_point))

dijk(1)
print(distance[-1])
