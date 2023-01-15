from queue import PriorityQueue
MAX = 100000
N,T = map(int, input().split())
visited = dict()
#N: 수빈
#T: 동생

que = PriorityQueue()#우선순위 큐
que.put([0,N])#우선순위(=시간), 값(=위치)

while que:
    cur = que.get()
    cur_time, cur_value = cur[0],cur[1]
    print("time:",cur_time,"pos:",cur_value)
    visited[cur_value] = 1
    
    if cur_value == T:
        print(cur_time)
        break
    
    if cur_value-1 not in visited:
        que.put([cur_time+1,cur_value-1])
        
    if cur_value*2-T<2:
        if cur_value*2 not in visited:
            que.put([cur_time,cur_value*2])
        
    if cur_value+1 not in visited:
        que.put([cur_time+1,cur_value+1])
