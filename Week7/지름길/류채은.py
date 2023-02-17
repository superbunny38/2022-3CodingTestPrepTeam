import heapq

N,D = map(int, input().split())#N: 지름길의 개수 D: 고속도로의 길이
graph = [[] for _ in range(D+1)]
distance = [float('inf')]*(D+1)#최소 비용 담을 공간

for idx in range(D):
    graph[idx].append((idx+1,1))

for _ in range(N):
    start, end, cost = map(int,input().split())
    if end>D:
        continue
    graph[start].append((end,cost))

#print(graph)

def dijk(start):
    q = []
    heapq.heappush(q,(0,start))#현재 cost는 0, 위치는 start
    distance[start] = 0
    while q:
        cost,cur_position = heapq.heappop(q)#튜플 앞 값(cost)을 기준으로 우선순위 정해짐
        #cost: 지금 위치(cur_position)까지 올 때의 cost
        if cost>distance[cur_position]:
            continue

        for i in graph[cur_position]:
            end_point,dist = i[0],i[1]
            if cost+dist < distance[end_point]:
                #cost+dist: 처음부터 지금 위치까지 비용(cost)+지금위치에서 endppint까지 비용(dist)
                distance[end_point] = cost+dist#최소 비용 갱신
                heapq.heappush(q,(cost+dist,end_point))

dijk(0)
print(distance[D])
