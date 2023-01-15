from collections import deque

MAX = 100000
N,K = map(int, input().split())
q = deque()
q.append([N,0])#position,time
visited = [0 for _ in range(MAX+1)]

while q:
    popped = q.popleft()
    cur_pos, cur_time = popped[0],popped[1]
    if cur_pos == K:
        print(cur_time)
        break
    visited[cur_pos] = 1
    
    #x2
    #print(cur_pos*2)
    if cur_pos*2 <= MAX and visited[cur_pos*2] ==0:
        q.appendleft([cur_pos*2,cur_time])
    #-1
    if 0<= cur_pos -1 <= MAX and visited[cur_pos-1] ==0:
        q.append([cur_pos-1,cur_time+1])
    #+1
    if 0<=cur_pos +1 <= MAX and visited[cur_pos+1] == 0:
        q.append([cur_pos+1, cur_time+1])
        
